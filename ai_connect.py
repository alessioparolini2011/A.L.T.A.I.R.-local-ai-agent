''''
This file create a connection with the Ollama Server running on http://localhost:11434 and sent one user prompt. 
'''



#import the library to speak with the AI model 

import requests

#putting in a variable the Ollama URL to speak with the model  --> DON'T CHANGE <--

URL = "http://localhost:11434/api/chat"

#creating the chat history

history = [
    {
        "role" : "system",
        "content" : "Sei un assistente AI dedicato alla conversazione. Sii conciso e colloquiale."
    }
]




def request(prompt):

    history.append({
        "role" : "user", 
        "content" : prompt
    })

    payload = {
    "model" : "qwen2.5:7b",
    "messages" : history,
    "options": {
        "num_predict" : 400,
        "temperature" : 0.4
    },
    "stream" : False
}

    #send the prompt to the AI model 

    req = requests.post(URL, json=payload)
    response = req.json()["message"]["content"]

    #save the response in the history

    history.append(
    {
        "role" : "assistant",
        "content" : response
    }
    )

    return response



