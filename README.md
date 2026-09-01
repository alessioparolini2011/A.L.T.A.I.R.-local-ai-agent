# This is A.L.T.A.I.R. (Autonoms Local Task Agent for Intelligent Reasoning)

A.L.T.A.I.R. is a AI assitant developed by Alessio Parolini. Is a open source software.

> [!WARNING]
> The project is still under development, many features will be added in future, so if you see bugs or have some adivces, don't wait to contact me on [my website](https://my-code-portfolio-ten.vercel.app/).
> Now only works in italian, my language, because is easier to me to try it and see if everything is ok. Other languagues will be added in future!

## Features:

- It runs **100% locally on your device**, using [Ollama models](https://ollama.com). **No data leave your PC!**

- Use a **vocal I/O system** using Vosk and Pyttsx4, that guarantee a quick and soft STT and TTS.

- It's based on a **double threading architecture**, so the performances are maximize

## How to use?

Good question. First at all, clone the repo on your PC. **Is recommended to don't install it on the C:/User/username, because it had to run with a PS command, so it's more safer install, for example, in the Desktop**

So first run in the terminal

`cd .\Desktop`

and then

`git clone https://github.com/alessioparolini2011/A.L.T.A.I.R.-local-ai-agent`

Now you have to install Ollama for use the local AI models. You can use

`winget install Ollama.Ollama`

When it's done, **open a new tab (don't close the current)** and run

`ollama serve`

**Open an another new tab (don't close the two precedent)**

`ollama run qwen2.5:7b-instruct `

> [!WARNING]
> This model needs about 6 GB on the RAM, but you can change it in ai_connect.py (line 40) with a smaller one (or bigger if you have a better hardware and you want better performance). Remember to change the terminal command too!

**Without closing tabs**, come back to the first one. It's time to run the file!

If you don't have Python installed, use

`winget install Python.Python.3.14`

(or the most recent version) in your terminal.

Install all required libraries with

`pip install requirements.txt`

And finally, run

`python main.py`

Enjoy!

## About me

Hi, I'm **Alessio Parolini**, a young developer based in Verona, Italy. This is my first important project on GitHub, so I'd be very happy if you **leave a star** and most important, if you want to gave my advices to improve myself. See [my profile](https://github.com/alessioparolini2011)
