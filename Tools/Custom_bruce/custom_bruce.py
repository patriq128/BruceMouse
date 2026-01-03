# Author: @patriq128

import itertools
import string
import time
import json
import os

from setup import term, timecount, stop, device_type

folder = os.path.dirname(os.path.abspath(__file__))

#Main
#---------------------------------------------------------------------------------------------------------
def custom_bruce():
    print("\033[2J\033[H", end="")
    print("""\033[32m Custom Bruce \033[0m""") # !Dont forget change NAME!
    print("\033[0m---------------------------------------------------------------------------------------------------------")
    print("""a) Manipulate save files
b) New file
c) Run save files""")
    print("\033[0m---------------------------------------------------------------------------------------------------------")

    customselect = input("Select:")
    if customselect == "a":
        show_files()

    elif customselect == "b":
        new_files()

    elif customselect == "c":
        run_files()

    elif customselect == "exit":
        stop()
        quit()
    else:
        print("\033[31m!Wrong Input!\033[0m")
        time.sleep(1)
        custom_bruce()
#---------------------------------------------------------------------------------------------------------

#Show files
#---------------------------------------------------------------------------------------------------------
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
        print("\033[31m!Wrong Input!\033[0m")
        time.sleep(1)
        show_files()

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
#---------------------------------------------------------------------------------------------------------

#New file
#---------------------------------------------------------------------------------------------------------
def new_files():
    print("New File") # Repair this later !
    print("\033[0m---------------------------------------------------------------------------------------------------------")
    namec = input("File Name:")

    CONFIG_PATH = os.path.join(folder, os.path.join(".", f"{namec}.json"))
    with open(CONFIG_PATH, "w") as f:
        pass

    print("Write the code with the symbols in help and when you are finish press Enter.")
    print("""b = bruce attack 1x
w = wait [-c = config] [-number = custom time]
m = manual [-text = custom text to write] [-e = enter]
r = repeat (use { to stard and } to end)""")
    print("""\033[31m!New comand mean "," !\033[0m""")

    program = input("Write program:")

    writepro = {"Program": program}

    with open(CONFIG_PATH, "w") as f:
        json.dump(writepro, f, indent=4)
#---------------------------------------------------------------------------------------------------------

#Run files
#---------------------------------------------------------------------------------------------------------
def bruce_attack():
    
    print("Bruce attack executed")


def wait_config():
    with open("config.json", "r") as f:
        config = json.load(f)
        speed = config["speed"]
    time.sleep(speed)
    print("Waiting using config")


def wait_custom(value: int):
    time.sleep(value)
    print(f"Waiting for {value}")


def manual_text(text: str):
    if term() == "1" or device_type() == "0":
        print(f"Manual text: {text}")
    else:
        pyautogui.typewrite(text)
        print(f"Manual text: {text}")


def manual_enter():
    if term() == "1" or device_type() == "0":
        print("Enter pressed")
    else:
        pyautogui.press("enter")
        print("Enter pressed")

def execute_command(cmd: str, arg=None):
    if cmd == "b":
        bruce_attack()

    elif cmd == "w":
        if arg == "c":
            wait_config()
        elif isinstance(arg, int):
            wait_custom(arg)
        else:
            raise ValueError("Invalid argument for w")

    elif cmd == "m":
        if arg == "e":
            manual_enter()
        elif isinstance(arg, str):
            manual_text(arg)
        else:
            raise ValueError("Invalid argument for m")

    else:
        raise ValueError(f"Unknown command: {cmd}")

def parse_and_run(program: str):
    tokens = program.replace(" ", "").split(",")
    i = 0
    last_block = []

    while i < len(tokens):
        token = tokens[i]

        if token.startswith("{"):
            block = token[1:]
            while i + 1 < len(tokens) and not tokens[i].endswith("}"):
                i += 1
                block += "," + tokens[i]

            if not tokens[i].endswith("}"):
                print("\033[31m!Warning: Block never closed with '}'\033[0m")
            else:
                block = block.rstrip("}")

            last_block = block.split(",")

            for t in last_block:
                run_token(t)

        elif token.isdigit() and i + 1 < len(tokens) and tokens[i + 1] == "r":
            if not last_block:
                print("\033[31m!Warning: Nothing to repeat\033[0m")
            else:
                count = int(token)
                for _ in range(count):
                    for t in last_block:
                        run_token(t)
            i += 1  # preskočíme "r"

        else:
            run_token(token)

        i += 1

def run_token(token: str):
    if "-" in token:
        cmd, arg = token.split("-", 1)
        # pokus previesť argument na číslo
        if arg.isdigit():
            arg = int(arg)
        execute_command(cmd, arg)
    else:
        execute_command(token)

def run_files():
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
        print("\033[31m!Wrong Input!\033[0m")
        time.sleep(1)
        show_files()

    index = int(selectc) - 1

    if index < 0 or index >= len(files):
        print("no file")
        return

    selected_file_path = files[index]

    print("Running:", selected_file_path)

    with open(selected_file_path, "r") as f:
        data = json.load(f)

    program = data["Program"]
    parse_and_run(program)
#---------------------------------------------------------------------------------------------------------
