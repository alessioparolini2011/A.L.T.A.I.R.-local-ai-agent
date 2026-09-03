''''This is the main file of the project. It imports the functions and objects from the other files and runs them in a double thread. The first thread is used to give a voice to the AI model, while the second thread is used to listen to the user and send the prompt to the AI model. The main thread waits for the TTS to finish before listening to the user again. This avoids a loop where the TTS and STT are running at the same time and creating a loop.
The main thread also handles the KeyboardInterrupt exception to terminate the program gracefully.'''

#Import the functions from the others files

from ttspeech import caller, switcher

from ai_connect import request

from sttext import hear


#importing the librarie to use asynchronous functions

import asyncio


#creating the main function 

async def main():

    print("Starting the program...")

    switcher.set() #set the switcher to True to let the STT to run

    try: 

        #start the asyncio gather

        async with asyncio.TaskGroup() as tg:

            tg.create_task(hear())
            tg.create_task(request())
            tg.create_task(caller())


        
    except KeyboardInterrupt:

        print("Program terminated by user.")


if __name__ == "__main__":

    asyncio.run(main())