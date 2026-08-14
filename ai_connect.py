''''
This file create a connection with the Ollama Server running on http://localhost:11434 and sent one user prompt. 
'''



#import the library to speak with the AI model 

import requests

#putting in a variable the Ollama URL to speak with the model  --> DON'T CHANGE <--

URL = "http://localhost:11434/api/generate"


def request():

    prompt = input("Fai una domanda all'IA: ")

    payload = {
    "model" : "llama3.2",
    "prompt" : prompt,
    "options": {
        "num_predict" : 400,
        "temperature" : 0.4
    },
    "stream" : False
}

    #send the prompt to the AI model 

    req = requests.post(URL, json=payload)
    response = req.json()["response"]

    return response



