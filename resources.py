'''
This file download and manage all the necessary resources (Vosk and PiperTTS model) automatically, so the user don't have to do it by himself
and there are no heavy files on the repo. 
'''

#importing the libraries to manage files, directory and downloads

import os 

import httpx as hx

import zipfile as zp

#creating the resources paths

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #get the user correct path

VOSK_PATH = os.path.join(BASE_DIR, "vosk-model")

VOSK_URL = "https://alphacephei.com/vosk/models/vosk-model-en-us-0.22-lgraph.zip"

PIPER_PATH = os.path.join(BASE_DIR, "pipertts-model")

PIPER_ONNX_URL = "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/ryan/medium/en_US-ryan-medium.onnx"

PIPER_JSON_URL = "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/ryan/medium/en_US-ryan-medium.onnx.json"

def vosk_installer(path, url):

    if os.path.exists(path): #check if is present (to avoid to install twice if the user run it again for some reason)

        print("Vosk directory already exists.")

        return path

    else: 

        request = hx.get(url, follow_redirects=True) #go to the url to download the required file, following possible server redirects

        print(f"Downloaded the vosk_model.zip from {url}")

        zip_dir = "vosk-model.zip"

        with open(zip_dir, "wb") as zip:

            zip.write(request.content) #saves the file on the disk

        if zp.is_zipfile(zip_dir): #check if is a zip (vosk case)

            with zp.ZipFile(zip_dir, mode="r") as archive:

                 archive.extractall("vosk-model")

                 print(f"Vosk resources successfully installed")

        else: 

            print("The directory is not a .zip. Check the Vosk model URL, probably is uncorrect.")
            
            os.remove(zip_dir) #remove the corrupt file and return None

            return None

        os.remove(zip_dir) #remove the file when is sure is closed

        return path


def piper_installer(path, url):

    file_name = url.split("/")[-1] #get the file name from the URL

    file_path = os.path.join(path, file_name)
    

    if os.path.exists(file_path): #check if is present (to avoid to install twice if the user run it again for some reason)
    
            print("PiperTTS directory already exists.")
    
            return path

    else:

        os.makedirs(path, exist_ok=True) #create the repo

        request = hx.get(url, follow_redirects=True) #go to the url to download the required file, following possible server redirects

        print(f"Downloaded {file_name}")

        with open(file_path, "wb") as file:

             file.write(request.content)

        return path


vosk_installer(VOSK_PATH, VOSK_URL)

piper_installer(PIPER_PATH, PIPER_JSON_URL)

piper_installer(PIPER_PATH, PIPER_ONNX_URL)

print("Finished")