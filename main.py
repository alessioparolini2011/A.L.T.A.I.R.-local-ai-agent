''''This is the main file. It groups together the functions by others files and call it. '''

# import functions from ttspeech.py and ai_connect.py files

from ttspeech import speech

from ai_connect import request

from sttext import ascolta


def main():

    while True:

        frase = ascolta()

        output = request(frase)

        speech(output)



if __name__ == "__main__":

    main()