#importing the libraries to create and play the response 

from gtts import gTTS

import pygame

import time

#initialazing the pygame mixer to play the audio 

pygame.mixer.init()


def speech(tts):

    #transforming the AI response into a audio file and playing it

    ai_speech = gTTS(text=tts, lang="it", slow=False)

    ai_speech.save("audio.mp3")

    pygame.mixer.music.load("audio.mp3")

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    


