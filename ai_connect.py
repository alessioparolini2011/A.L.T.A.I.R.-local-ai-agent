''''
This file create a connection with the Ollama Server running on http://localhost:11434 and sent one user prompt. 

Also save the response in a history variable to create a conversation with the AI model.

Finally put the response in a variable to be used in the main.py file and then sent to the ttspeech.py file to be spoken by the computer.
'''



#import the library to speak with the AI model and the FIFO list

import requests

import json 

from shared import r

#putting in a variable the Ollama URL to speak with the model  --> DON'T CHANGE <--

URL = "http://localhost:11434/api/chat"

#creating the chat history

history = [
    {
        "role" : "system",
        "content" : "You are a useful AI assistant that helps the user in his tasks and daily life. Speak in a friendly way and with shorts and clear answers. Answer in Italian."
    }
]



def request(prompt):

    history.append({
        "role" : "user", 
        "content" : prompt
    })

    payload = {
    "model" : "qwen2.5:7b-instruct",
    "messages" : history,
    "options": {
        "num_predict" : 500,
        "temperature" : 0.1
    },
    "stream" : True
}

    #send the prompt to the AI model 

    req = requests.post(URL, json=payload, stream=True)

    #get the response from the AI model 

    response = ""

    #creating a list of punctuation to check if the AI model response contains some punctuation to avoid the AI model to speak in a robotic way

    punctuation = [".", "!", "?" ,",", ";", ":"]

    for line in req.iter_lines():

        if line:

            chunk = json.loads(line.decode("utf-8"))

            token = chunk['message']['content']

            print(token)

            #check if the token contains some puntuaction to avoid the AI model to speak in a robotic way

            if any(p in token for p in punctuation):

                for p in punctuation:

                    if p in token:

                        parts = token.split(p)

                        response += parts[0] + p

                        r.put(response)

                        response = parts[1]

                        break

            else:

                response += token


    r.put(None) #put a None in the FIFO list to signal the end of the response


    history.append({
        "role" : "assistant",
        "content" : response
    })