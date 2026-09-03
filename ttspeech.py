'''
This file is used to give a voice to the AI model. 
It uses the pyttsx4 library to convert the text response from the AI model into speech.
It runs in a separate thread, so can start talking while the AI response is still being generated.
'''


#importing the libraries to play the audio response from the AI model and to use asynchronous functions

import pyttsx4

import asyncio

#asyncio FIFO list, blocker and switcher to avoid loops

switcher = asyncio.Event()

blocker = False

res = asyncio.Queue() #creating a FIFO list that to get AI splitted response from ai_connect


async def caller(): #to activate the TTS function in a separate thread

    while True:

        phrase =  await res.get()

        if phrase is not None:

            if phrase.strip():

                await asyncio.to_thread(speak, phrase)

        else: 

            print("A.L.T.A.I.R. finished. Is your turn now. ")

            switcher.set()

        
def speak(text): #to give a voice to the AI model

    #initializing engine, voice and speed (rate)

    engine = pyttsx4.init()

    engine.setProperty("rate", 125) #set the speed of the voice

    voice = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0"

    engine.setProperty("voice", voice )

    engine.say(text)

    engine.runAndWait()