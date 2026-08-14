''''This is the main file. It groups together the functions by others files and call it. '''

# import functions from ttspeech.py and ai_connect.py files

from ttspeech import speech

from ai_connect import request


def main():

    # save the ai response and transforms it in a audio file

    ai_response = request()

    speech(ai_response)


if __name__ == "__main__":

    main()