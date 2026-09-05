'''
This file is used to give a voice to the AI model. 
It runs in a subprocess the piper.exe, for a natural but fast and light response. 
'''

#importing the libraries to synthesize and play the audio response from the AI model and to use asynchronous functions

import asyncio

import piper

import sounddevice as sd

import wave

import time #for a micro-pause between every phrase

import soundfile as sf

import io #this library create a bytes buffer, to save temporarily the piper audio in the RAM instead of savwe it on the SSD


#asyncio FIFO list, blocker and switcher to avoid loops

switcher = asyncio.Event()

res = asyncio.Queue() #creating a FIFO list that to get AI splitted response from ai_connect


async def caller(): #get data from ai_connect and send to piper to synthesize the audio and call speaker() to play it

    voice = piper.PiperVoice.load("piper_model/en_US-ryan-medium.onnx") #initializating the piper model

    while True:

        phrase = await res.get()

        if phrase is not None:

            buffer = io.BytesIO() #creating the bytes buffer 

            with wave.open(buffer, "wb") as wav_file:
                voice.synthesize_wav(phrase, wav_file)

            buffer.seek(0) #put the read cursor in the first position

            audio, samplerate = sf.read(buffer)

            await asyncio.to_thread(speaker, audio, samplerate )

            res.task_done()

        else:

            switcher.set()

            res.task_done()

            print("A.L.T.A.I.R. is ready to listen, please speak...")


def speaker(data, samplerate):

    sd.play(data=data, samplerate=samplerate)

    sd.wait()

    time.sleep(0.25)