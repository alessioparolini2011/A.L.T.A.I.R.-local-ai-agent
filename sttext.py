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

model = Model("vosk_model")

reco = KaldiRecognizer(model, 16000)

async def hear():

    #getting the event loop to use it in the callback function

    loop = asyncio.get_event_loop()

    #creating the function to get the audio from the microphone and put it in the FIFO list

    def callback(indata, frames, time, status): 

        #putting the audio pack in the list

        loop.call_soon_threadsafe(pack.put_nowait, indata)

    #starts to get datas from microphone

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=4096,
        dtype="int16",
        channels=1, 
        callback=callback,
    ):

        print("A.L.T.A.I.R. is ready to listen, please speak...")

        while True: 

            data = await pack.get()

            if not switcher.is_set():

                pack.task_done()

                continue 

            b_data = bytes(data)

            #Check if the voice input is end (on an another thread because is a heavy operation)
            is_final = await asyncio.to_thread(reco.AcceptWaveform, b_data)

            if is_final: #if understand the input is finish, use the model to transcribe it

                voice = json.loads(reco.Result())
                text = voice["text"]

                if text:

                    print(f"You said: {text}")

                    await message.put(text) #put the transcribed text in the FIFO list to be used by ai_connect.py to send the prompt to the AI model