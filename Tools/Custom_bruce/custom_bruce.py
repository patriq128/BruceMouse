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
    files = [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.endswith(".json")
    ]

    if not files:
        print("\033[31m!No files!\033[0m")
        return

    for i, path in enumerate(files, start=1):
        name = os.path.basename(path)[:-5] 
        print(f"{i}. {name}")

    print("\033[0m---------------------------------------------------------------------------------------------------------")
    selectc = input("File number: ")

    if selectc == "exit":
        stop()
        quit()

    if not selectc.isdigit():
        print("")

    index = int(selectc) - 1

    if index < 0 or index >= len(files):
        print("no file")
        return

    selected_file_path = files[index]

    print("Selected file:", selected_file_path)
    print("\033[0m---------------------------------------------------------------------------------------------------------")
    print("""a) Delete file
b) Open file""")
    optionsele = input("Choose optino:")

    if optionsele == "a":
        os.remove(selected_file_path)
    elif optionsele == "b":
        with open(selected_file_path, "r") as f:
            data = json.load(f)
        print(data["Program"])

def new_files():
    print("New File") # Repair this later !
    print("\033[0m---------------------------------------------------------------------------------------------------------")
    namec = input("File Name:")

    CONFIG_PATH = os.path.join(folder, os.path.join(".", f"{namec}.json"))
    with open(CONFIG_PATH, "w") as f:
        pass

    print("Write the code with the symbols in help and when you are finish press Enter.")
    print("""""")
    print("\033[31m!New comand mean space and , !\033[0m")

    program = input("Write program:")

    writepro = {"Program": program}

    with open(CONFIG_PATH, "w") as f:
        json.dump(writepro, f, indent=4)
