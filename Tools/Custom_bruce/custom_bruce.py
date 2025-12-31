# Author: @patriq128

import itertools
import string
import time
import json
import os

from setup import term, timecount, stop, device_type

folder = os.path.dirname(os.path.abspath(__file__))

def custom_bruce():
    print("\033[2J\033[H", end="")
    print("""\033[32m Custom Bruce \033[0m""") # !Dont forget change NAME!
    print("\033[0m---------------------------------------------------------------------------------------------------------")
    print("""a) Show save files
b) New file
c) Run save files""")
    print("\033[0m---------------------------------------------------------------------------------------------------------")

    customselect = input("Select:")
    if customselect == "a":
        show_files()

    elif customselect == "b":
        new_files()

    elif customselect == "exit":
        stop()
        quit()
    else:
        print("\033[31m!Wrong Input!\033[0m")
        time.sleep(1)
        custom_bruce()

def show_files():

    json_files = [f[:-5] for f in os.listdir(folder) if f.endswith('.json')]

    if not json_files:
        print("\033[31m!No files!\033[0m")
    else:
        for idx, name in enumerate(json_files, start=1):
            print(f"{idx}. {name}")

def new_files():
    print("New File")
    print("\033[0m---------------------------------------------------------------------------------------------------------")
    namec = input("File Name:")

    CONFIG_PATH = os.path.join(folder, os.path.join(".", f"{namec}.json"))
    with open(CONFIG_PATH, "w") as f:
        pass
