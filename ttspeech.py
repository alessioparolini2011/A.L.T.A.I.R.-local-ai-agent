#importing the librarie to create and play the response 

import pyttsx4

#initialazing the tts engine and some others funcitons

engine = pyttsx4.init()

engine.setProperty("rate", 120)

voice = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0"

engine.setProperty("voice", voice )

def speech(tts):

    engine.say(tts)

    engine.runAndWait()