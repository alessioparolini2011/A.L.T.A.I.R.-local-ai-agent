'''
Here you can find the global variables and objects shared in the entire project
'''

import queue 

import threading

r = queue.Queue()

#creating a  threading switcher to get sure TTS and STT doesn't run at the same time, to avoid the AI model to hear its own voice and create a loop.

switcher = threading.Event()