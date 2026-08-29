#importing the librarie to create and play the response 

import pyttsx4

from shared import r, switcher

#initialazing the tts engine and some others funcitons



def speech():

    #initialazing the tts engine and some others funcitons

    engine = pyttsx4.init()

    engine.setProperty("rate", 120)

    voice = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0"

    engine.setProperty("voice", voice )

    print("Secondary TTS is running...")

    while True:

        tts= r.get()

        if tts == None:

            switcher.clear() #if the TTS is finished, set the switcher to False to let the STT to run

            continue

        else: 

            switcher.set() #if the TTS is running, set the switcher to True to avoid the STT to run and create a loop

            engine.say(tts)

            engine.runAndWait()