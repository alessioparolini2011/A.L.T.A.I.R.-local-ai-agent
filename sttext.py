import queue

from vosk import Model, KaldiRecognizer

import json 

import sounddevice as sd

#creating the fifo object

q = queue.Queue()

def callback(indata, frames, time, status):

    #putting the audio pack in the list 

    q.put(bytes(indata))

    return frames, time, status


def ascolta():

    model = Model("model")

    reco = KaldiRecognizer(model, 16000)

    #starts toget datas from microphone

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype="int16",
        channels=1, 
        callback=callback,
    ):

        #deleting the audio sd registered before I start to speak 

        with q.mutex:
            q.queue.clear()

        print("IA in ascolto...")

        
        while True: 

            #put every audio block in the FIFO object

            data = q.get()

            #if understands the voice input is end, use the model to transcribe it

            if reco.AcceptWaveform(data):

                voice = json.loads(reco.Result())

                text = voice["text"]

                if text:

                    print(f"Hai detto: {text}")
                    return text


    