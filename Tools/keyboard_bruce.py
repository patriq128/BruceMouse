import itertools
import string
import time
import threading
import os
import sys

from setup import term, timecount, stop, device_type

with open("config.txt", "r") as f:
        speed = f.read()


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
            elif pen == "home":
                main()
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
            import pyautogui
            if term() == "1":
                print("Only Visulation mode")
                time.sleep(4)
                for conbinatione in conbination:
                    print(''.join(conbinatione))
                    time.sleep(float(speed))
                stop()
                quit()
            else:
                print("Choose the site")
                time.sleep(4)
                for conbinatione in conbination:
                    print(''.join(conbinatione))
                    pyautogui.typewrite(conbinatione)
                    pyautogui.press("enter")
                    time.sleep(float(speed))
                stop()
                quit()
