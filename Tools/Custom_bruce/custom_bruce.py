# Author: @patriq128

import itertools
import string
import time
import json
import os

from setup import term, timecount, stop, device_type

def custom_bruce():
    print("\033[2J\033[H", end="")
    print("""\033[32m Custom Bruce \033[0m""") # !Dont forget change NAME!
    print("\033[0m---------------------------------------------------------------------------------------------------------")
    print("""a) Show save files
b) Run save files
c) New file""")
    print("\033[0m---------------------------------------------------------------------------------------------------------")

    customselect = input("Select:")
    if customselect == "a":
        show_files()

    elif customselect == "exit":
        stop()
        quit()
    else:
        print("\033[31m!Wrong Input!\033[0m")
        time.sleep(1)
        custom_bruce()

def show_files():

    folder = os.path.dirname(os.path.abspath(__file__))

    json_files = [f[:-5] for f in os.listdir(folder) if f.endswith('.json')]

    if not json_files:
        print("\033[31m!No files!\033[0m")
    else:
        for idx, name in enumerate(json_files, start=1):
            print(f"{idx}. {name}")
