# Author: @patriq128
import itertools
import string
import time
import threading
import os
import sys
from setup import term, timecount, stop, device_type

# Setup tools
# ---------------------------
from Tools.keyboard_bruce import keyboard_bruce

try:

    #Setup Time
    start_time = time.time()
    
    #Setting time
    timer_thread = threading.Thread(target=timecount, daemon=True)
    timer_thread.start()
# ------------------------------------------------------------------------------------------------------------------------------------- 

# Process
# ------------------------------------------------------------------------------------------------------------------------------------- 
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
                                
        else:
            print("\033[31mSorry Virtual keyboard work only on desktop. Maybe sometimes this gonna work >:3\033[0m")
            time.sleep(4)
            for conbinatione in conbination:
                print(''.join(conbinatione))
                time.sleep(float(speed))
            stop()
            quit()
# ------------------------------------------------------------------------------------------------------------------------------------- 

# Math
# ------------------------------------------------------------------------------------------------------------------------------------- 
    def math():
            print("\033[2J\033[H", end="")
            print("""\033[32m .d8888b.           888                   888          888    d8b                   
d88P  Y88b          888                   888          888    Y8P                   
888    888          888                   888          888                          
888         8888b.  888  .d8888b 888  888 888  8888b.  888888 888  .d88b.  88888b.  
888            "88b 888 d88P"    888  888 888     "88b 888    888 d88""88b 888 "88b 
888    888 .d888888 888 888      888  888 888 .d888888 888    888 888  888 888  888 
Y88b  d88P 888  888 888 Y88b.    Y88b 888 888 888  888 Y88b.  888 Y88..88P 888  888 
 "Y8888P"  "Y888888 888  "Y8888P  "Y88888 888 "Y888888  "Y888 888  "Y88P"  888  888 
                                                                                    
                                                                                    
                                                                                    """)
            print("""░█▀▄░█▀▄░█░█░█▀▀░█▀▀
░█▀▄░█▀▄░█░█░█░░░█▀▀
░▀▀░░▀░▀░▀▀▀░▀▀▀░▀▀▀""")
            print("\033[0m---------------------------------------------------------------------------------------------------------")
            
            world1 = input("Type the passworld:")
            
            if world1 == "exit":
                stop()
                quit()
            elif world1 == "home":
                main()
            else:
                world = world1
        
            chars = 0

            has_lower = any(c.islower() for c in world)
            has_upper = any(c.isupper() for c in world)
            has_digit = any(c.isdigit() for c in world)
            has_symbol = any(c in string.punctuation for c in world)

            if has_lower:
                chars += len(string.ascii_lowercase)
            if has_upper:
                chars += len(string.ascii_uppercase)
            if has_digit:
                chars += len(string.digits)
            if has_symbol:
                chars += len(string.punctuation)

            total = chars ** len(world)
            print(f"Possibilitys: {total:,}")
# ------------------------------------------------------------------------------------------------------------------------------------- 

# Help
# ------------------------------------------------------------------------------------------------------------------------------------- 
    def help():
        os.system('printf "\\033[9;1t"')
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[2J\033[H", end="")
        print("""\033[32m██╗  ██╗███████╗██╗     ██████╗ 
██║  ██║██╔════╝██║     ██╔══██╗
███████║█████╗  ██║     ██████╔╝
██╔══██║██╔══╝  ██║     ██╔═══╝ 
██║  ██║███████╗███████╗██║     
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     """)
        print("\033[0m---------------------------------------------------------------------------------------------------------")
        print("""a) Info
b) Keyboard Bruce
c) Calculate Bruce
d) Config""")
        print("\033[0m---------------------------------------------------------------------------------------------------------")
        helps = input("select:")
        
        if helps == "a":
            print("Info")
        elif helps == "b":
            print("Keyboard Bruce")
        elif helps == "c":
            print("Calculate Bruce")
        elif helps == "d":
            print("Config")
        elif helps == "exit":
            stop()
            quit()
        elif helps == "home":
            main()
        else:
            print("\033[31m!Wrong Input!\033[0m")
            time.sleep(1)
            help()
# ------------------------------------------------------------------------------------------------------------------------------------- 

# Config
# ------------------------------------------------------------------------------------------------------------------------------------- 
    def data():
        os.system('printf "\\033[9;1t"')
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[2J\033[H", end="")
        print("""\033[32m                                    
 ▄▄▄▄▄▄▄               ▄▄           
███▀▀▀▀▀              ██  ▀▀        
███      ▄███▄ ████▄ ▀██▀ ██  ▄████ 
███      ██ ██ ██ ██  ██  ██  ██ ██ 
▀███████ ▀███▀ ██ ██  ██  ██▄ ▀████ 
                                 ██ 
                               ▀▀▀  \033[0m""")
        global speed
        with open("config.txt", "r") as f:
            speed = f.read()
            speed = float(speed)
            print(f"Actual speed value: {speed:,}")
        time.sleep(0.5)
        inputtxt = input("New speed value:")
        if inputtxt == "exit":
            stop()
            quit()
        elif inputtxt == "home":
            main()
        elif any(c.isalpha() for c in inputtxt):
            print("\033[31m!Only digits!\033[0m")
            time.sleep(1)
            data()
        else:
            with open("config.txt", "w") as f:
                f.write(str(inputtxt))
            data()
# ------------------------------------------------------------------------------------------------------------------------------------- 

# Main
# ------------------------------------------------------------------------------------------------------------------------------------- 
    def main():
        os.system('printf "\\033[9;1t"')
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[2J\033[H", end="")
        print("""\033[35m ███████████                                         ██████   ██████                                     
▒▒███▒▒▒▒▒███                                       ▒▒██████ ██████                                      
 ▒███    ▒███ ████████  █████ ████  ██████   ██████  ▒███▒█████▒███   ██████  █████ ████  █████   ██████ 
 ▒██████████ ▒▒███▒▒███▒▒███ ▒███  ███▒▒███ ███▒▒███ ▒███▒▒███ ▒███  ███▒▒███▒▒███ ▒███  ███▒▒   ███▒▒███
 ▒███▒▒▒▒▒███ ▒███ ▒▒▒  ▒███ ▒███ ▒███ ▒▒▒ ▒███████  ▒███ ▒▒▒  ▒███ ▒███ ▒███ ▒███ ▒███ ▒▒█████ ▒███████ 
 ▒███    ▒███ ▒███      ▒███ ▒███ ▒███  ███▒███▒▒▒   ▒███      ▒███ ▒███ ▒███ ▒███ ▒███  ▒▒▒▒███▒███▒▒▒  
 ███████████  █████     ▒▒████████▒▒██████ ▒▒██████  █████     █████▒▒██████  ▒▒████████ ██████ ▒▒██████ 
▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒       ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒   ▒▒▒▒▒▒  ▒▒▒▒▒     ▒▒▒▒▒  ▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒ ▒▒▒▒▒▒   ▒▒▒▒▒▒  """)
        print("\033[0mAuthor: @patriq128")
        print("\033[94mWelcome in BruceMouse the only place where you can do your best :)")
        print("\033[31m!!Only for education!!")
        print("""\033[0m*type "exit" for exit :3 """)
        
        if device_type() == "1":
            print("\033[32mDevice type: Desktop")
        else:
            print("\033[32mDevice type: Phone")
            
        if term() == "1":
            print("Visualation mode")
        
        print("\033[0m---------------------------------------------------------------------------------------------------------")
        
        #Asking :3
        print("What type of bruce you want?")
        print("""1.) Keyboard Bruce
2.) Calculate Bruce
3.) Help
*) Config""")
        present = input("Select:")

        #Main Part
        if present == "1":
            keyboard_bruce()
        
        elif present == "2":
            math()
        
        elif present == "3":
            help()
        
        elif present == "*":
            print("Opening config file")
            data()
    
        elif present == "exit":
            stop()
            quit()  
            
        else:
            print("\033[31m!Wrong Input!\033[0m")
            time.sleep(1)
            main()           
# -------------------------------------------------------------------------------------------------------------------------------------     
    
# Main controling System
# -------------------------------------------------------------------------------------------------------------------------------------     
    def maind():
        if "--key" in sys.argv:
            keyboard_bruce()
        elif "--calc" in sys.argv:
            math()
        elif "--help" in sys.argv:
            help()
        elif "--conf" in sys.argv:
            data()
        else:
            main()        
# -------------------------------------------------------------------------------------------------------------------------------------     

# Just Run
# -------------------------------------------------------------------------------------------------------------------------------------     
    maind()
# -------------------------------------------------------------------------------------------------------------------------------------     

except KeyboardInterrupt:
    stop()
    quit()