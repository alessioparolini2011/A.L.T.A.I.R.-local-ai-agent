''''
This file create a connection with the Ollama Server running on http://localhost:11434 and sent one user prompt. 

Also save the response in a history variable to create a conversation with the AI model.

Finally put the response in a FIFO list to be used by the TTS function to give a voice to the AI model.
'''

#importing the libraries to create a connection with the Ollama Server, split response and send the user prompt

import httpx

import asyncio

import json 

import re

from ttspeech import res as r, switcher

from sttext import message as m

#putting in a variable the Ollama URL to speak with the model  --> DON'T CHANGE <--

URL = "http://localhost:11434/api/chat"

#creating the chat history

history = [
    {
        "role" : "system",
        "content" : "You are a useful AI assistant that helps the user in his tasks and daily life. Speak in a friendly way and with shorts and clear answers. Answer in Italian."
    }
]



async def request():

    while True: 

        prompt = await m.get()

        m.task_done()

        switcher.clear()

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

        #create a variable to put in the history.append, one for split the response and a regex pattern
        
        response = ""

        buffer = ""

        splitter = re.compile(r"([^;.:?!]*[;.:?!])")
        

        #send the prompt to the AI model 

        async with httpx.AsyncClient(timeout=None) as client:

            async with client.stream("POST", URL, json=payload) as req:

                async for line in req.aiter_lines():

                    if line:

                        chunk = json.loads(line)

                        token = chunk['message']['content']

                        response += token 

                        buffer += token


                    #check if the token contains some puntuaction to split response and send it to the TSS before the whole response is ready

                        part = re.findall(splitter, buffer) #find a complete sentence in the buffer to send it to the TTS

                        for p in part:

                            if p.strip():

                                print(p)

                                await r.put(p) #send to the TTS 

                                buffer = buffer[len(p):] 

        if buffer: #maybe the last phrase don't end with a puntuaction, so this is a last check to send all the response

            await r.put(buffer)

            await r.put(None)

        else:

            await r.put(None) #put a None in the FIFO list to signal the end of the response


        history.append({
            "role" : "assistant",
            "content" : response
        })

        if len(history) > 11:

            del history[2:4] #delete the oldest messages to avoid the history to be too long and the AI model to forget the context of the conversation but keeps the system prompt.