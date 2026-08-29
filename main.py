''''This is the main file. It groups together the functions by others files and call it. Also manage double threading. '''

#Import the functions and objects from the other files

from ttspeech import speech

from ai_connect import request

from sttext import hear

import threading

from shared import switcher

#initialazing double thread

speakT = threading.Thread(target=speech, args=(), daemon=True)


def main():

    speakT.start()

    while True:

        phrase = hear()

        request(phrase)

        switcher.wait()


if __name__ == "__main__":

    main()