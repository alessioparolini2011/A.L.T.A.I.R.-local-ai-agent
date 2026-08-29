import queue
from vosk import Model, KaldiRecognizer
import json 
import sounddevice as sd

#creating the fifo object
q = queue.Queue()

#initializing the vosk model
model = Model("model")
reco = KaldiRecognizer(model, 16000)

def callback(indata, frames, time, status):
    #putting the audio pack in the list 
    if status:
        print(status)
    q.put(bytes(indata))

def hear():

    #starts to get datas from microphone
    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype="int16",
        channels=1, 
        callback=callback,
    ):

        #deleting the audio sd registered before I start to speak 
        while not q.empty():
            q.get()

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