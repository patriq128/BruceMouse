import itertools
import string
import time
import threading
import os
import sys
import json

#Setup Time
start_time = time.time()

def term():
    if "--vis" in sys.argv:
        return "1"
    
#Controling config
file_name = "config.json"
if not os.path.exists(file_name):
    with open(file_name, "w") as f:
        json.dump({"speed": 0.5}, f, indent=4)

#Time counting
def timecount():
    while True:
        elapsed = time.time() - start_time
        time.sleep(1)
    
#Stop
def stop():
    global objective
    objective = round(time.time() - start_time, 2)
    print("\033[2J\033[H", end="")
    print("Good bye!")
    text = f"\033[36mfinal running time: {objective:,}'s\033[0m"

    text_len = 0
    i = 0
    while i < len(text):
        if text[i] == "\033":
            while i < len(text) and text[i] != "m":
                i += 1
            i += 1
        else:
            text_len += 1
            i += 1

    width = text_len + 30
    height = 5

    for y in range(height):
        if y == 0 or y == height - 1:
            print("+" + "-" * (width - 2) + "+")
        elif y == height // 2:
            pad_left = (width - 2 - text_len) // 2
            pad_right = (width - 2 - text_len) - pad_left
            print("|" + " " * pad_left + text + " " * pad_right + "|")
        else:
            print("|" + " " * (width - 2) + "|")


def device_type():
    if os.path.exists("/data/data/com.termux"):
        return "0"
    else:
        return "1"
    
#Setting time
timer_thread = threading.Thread(target=timecount, daemon=True)
timer_thread.start()
