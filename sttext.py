import asyncio

from vosk import Model, KaldiRecognizer

import json 

import sounddevice as sd

from ttspeech import switcher


#creating the FIFO list to get the audio pack from the microphone

pack = asyncio.Queue()

#creating the FIFO list to send the audio to ai_connect.py as the prompt to the AI model

message = asyncio.Queue()

#initializing the vosk model

model = Model("model")

reco = KaldiRecognizer(model, 16000)

async def hear():

    #getting the event loop to use it in the callback function

    loop = asyncio.get_event_loop()

    #creating the function to get the audio from the microphone and put it in the FIFO list

    def callback(indata, frames, time, status): 

        #putting the audio pack in the list 
        
        if status:
            print(status)

        loop.call_soon_threadsafe(pack.put_nowait, bytes(indata))

    #starts to get datas from microphone

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype="int16",
        channels=1, 
        callback=callback,
    ):

        #deleting the audio sd registered before I start to speak 
        while not pack.empty():
            pack.get()

            pack.task_done()


        print("A.L.T.A.I.R. is ready to listen, please speak...")
        
        while True: 

            #put every audio block in the FIFO object
            data = await pack.get()

            if not switcher.is_set():

                continue

            #if understands the voice input is end, use the model to transcribe it
            if reco.AcceptWaveform(data):

                voice = json.loads(reco.Result())
                text = voice["text"]

                if text:

                    print(f"You said: {text}")

                    await message.put(text) #put the transcribed text in the FIFO list to be used by ai_connect.py to send the prompt to the AI model