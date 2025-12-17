import time
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
        with open("Tools/config.txt", "r") as f:
            speed = f.read()
            speed = speed
            print("Actual speed value:")
            print(speed)
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
            with open("Tools/config.txt", "w") as f:
                f.write(str(inputtxt))
