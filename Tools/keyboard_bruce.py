# Author: @patriq128

import itertools
import string
import time
import json
import platform
import subprocess

from setup import term, timecount, stop, device_type, what_OS

with open("config.json", "r") as f:
    config = json.load(f)
    speed = config["speed"]

def keyboard_bruce():
        global char
        print("\033[2J\033[H", end="")
        print("""\033[32m██╗  ██╗███████╗██╗   ██╗██████╗  ██████╗  █████╗ ██████╗ ██████╗ 
██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔══██╗
█████╔╝ █████╗   ╚████╔╝ ██████╔╝██║   ██║███████║██████╔╝██║  ██║
██╔═██╗ ██╔══╝    ╚██╔╝  ██╔══██╗██║   ██║██╔══██║██╔══██╗██║  ██║
██║  ██╗███████╗   ██║   ██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ """)
        print("""                                                              
█████▄ ▄▄▄▄  ▄▄ ▄▄  ▄▄▄▄ ▄▄▄▄▄ 
██▄▄██ ██▄█▄ ██ ██ ██▀▀▀ ██▄▄  
██▄▄█▀ ██ ██ ▀███▀ ▀████ ██▄▄▄                                \033[0m""")
        print("\033[0m---------------------------------------------------------------------------------------------------------")
        print("""Characters in bruce:
          
a) Lowercase
b) Uppercase
c) Digits
d) Everything
""")
        print("\033[0m---------------------------------------------------------------------------------------------------------")
        pen = input("typle select:")
        if pen == "a":
            char = string.ascii_lowercase
        elif pen == "b":
            char = string.ascii_uppercase
        elif pen == "c":
            char = string.digits
        elif pen == "d":
            char = string.ascii_lowercase + string.ascii_uppercase + string.digits
        elif pen == "exit":
            stop()
            quit()
        else:
            print("\033[31m!Wrong Input!\033[0m")
            time.sleep(1)
            keyboard_bruce()
        process()


def process():
        numberp = input("Number input:")
        if any(c.isalpha() for c in numberp):
            print("\033[31m!Only digits!\033[0m")
            time.sleep(1)
            process()
        else:
            prosessn = int(numberp)
            
        #calculation
        conbination = itertools.product(char, repeat=prosessn)
        #main
        if device_type() == "1":
            if term() == "1":
                print("Only Visulation mode")
                time.sleep(4)
                for conbinatione in conbination:
                    print(''.join(conbinatione))
                    time.sleep(float(speed))
                stop()
                quit()
            else:
                try:
                    import pyautogui

                    print("Choose the site")
                    time.sleep(4)
                    for conbinatione in conbination:
                        print(''.join(conbinatione))
                        pyautogui.typewrite(conbinatione)
                        pyautogui.press("enter")
                        time.sleep(float(speed))
                    stop()
                    quit()

                except ImportError:
                    print("""\033[0mYou dont have libary \033[91m"pyautogui" """)
                    print("\033[92mStart download?")
                    y_or_n = input("""\033[92m"y"\033[0m/\033[91m"n"\033[0m: """)
                    if y_or_n == "y":
                        download()
                    elif y_or_n == "n":
                        print("\033[91mWithout libarys its dont gonna work")
                        print("\033[0mSwitching to visual mode")
                        time.sleep(2)

        else:
            print("\033[31mSorry virtual keyboard work only on desktop. Maybe sometimes this gonna work >:3\033[0m")
            print("Only Visulation mode")
            time.sleep(4)
            for conbinatione in conbination:
                print(''.join(conbinatione))
                time.sleep(float(speed))
            stop()
            quit()


def download():
    print("\033[0mDevice OS: \033[92m" + what_OS() + "\033[94m")
    if what_OS() in ["MacOS", "Windows"]:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui"])
    elif what_OS() == "Linux":
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui", "--break-system-packages"])
    else:
        print("\033[91mSorry, something went wrong")
    
    print("\033[91mDone")
    time.sleep(1)
    main()
