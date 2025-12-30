# Author: @patriq128

import time
import json
from setup import timecount, stop

def config():
    while True:
        print("\033[2J\033[H", end="")
        print("""\033[32m                                    
    ▄▄▄▄▄▄▄               ▄▄           
    ███▀▀▀▀▀              ██  ▀▀        
    ███      ▄███▄ ████▄ ▀██▀ ██  ▄████ 
    ███      ██ ██ ██ ██  ██  ██  ██ ██ 
    ▀███████ ▀███▀ ██ ██  ██  ██▄ ▀████ 
                                    ██ 
                                ▀▀▀  \033[0m""")
        with open("config.json", "r") as f:
            config = json.load(f)
            print("Speed:", config["speed"])
        inputtxt = input("New speed value:")
        if inputtxt == "exit":
            stop()
            quit()
        elif inputtxt == "home":
            return
        elif any(c.isalpha() for c in inputtxt):
            print("\033[31m!Only digits!\033[0m")
            time.sleep(1)
            continue
        else:
            config["speed"] = float(inputtxt)

            with open("config.json", "w") as f:
                json.dump(config, f, indent=4)
