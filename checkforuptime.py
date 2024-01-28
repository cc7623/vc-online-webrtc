import subprocess
from time import sleep
from threading import Thread
import os

def start():
    os.system("start.py")

while True:
    processes = subprocess.Popen('tasklist', stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()[0]

    if "py.exe" in str(processes):
        pass
    else:
        start()

    sleep(5)

