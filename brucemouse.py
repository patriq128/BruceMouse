# Author: @patriq128
import itertools
import string
import time
import threading
import os
import sys

try:

# Some setup things
# -------------------------------------------------------------------------------------------------------------------------------------     
    def term():
        if "--vis" in sys.argv:
            return "1"
    
    #Setup Time
    start_time = time.time()
    
    #Controling config
    file_name = "config.txt"
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            f.write("0.05")

    #Read config file
    with open("config.txt", "r") as f:
        speed = f.read()

    #Config setting
    def data():
        global speed
        with open("config.txt", "r") as f:
            speed = f.read()
            print(speed)
        time.sleep(0.5)
        inputtxt = input("speed value:")
        if inputtxt == "exit":
            
            main()
            choosebruce()
        else:
            with open("config.txt", "w") as f:
                f.write(str(inputtxt))
            data()

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
# ------------------------------------------------------------------------------------------------------------------------------------- 
        
# Keyboard Bruce
# -------------------------------------------------------------------------------------------------------------------------------------        
    def keyboard_bruce():
            global znaky
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
                znaky = string.ascii_lowercase
            elif pen == "b":
                znaky = string.ascii_uppercase
            elif pen == "c":
                znaky = string.digits
            elif pen == "d":
                znaky = string.ascii_lowercase + string.ascii_uppercase + string.digits
            elif pen == "exit":
                stop()
                quit()
            else:
                print("\033[31m!Wrong Input!\033[0m")
                time.sleep(1)
                keyboard_bruce()
            process()
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
            
            world = input("Type the passworld:")
        
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
        else:
            print("\033[31m!Wrong Input!\033[0m")
            time.sleep(1)
            help()
 # ------------------------------------------------------------------------------------------------------------------------------------- 
        
    #Main screen
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

    def process():
        pocet = int(input("Number input:"))
        #calculation
        kombinacie = itertools.product(znaky, repeat=pocet)
        #main
        if device_type() == "1":
            import pyautogui
            if term() == "1":
                print("Only Visulation mode")
                time.sleep(4)
                for kombinacia in kombinacie:
                    print(''.join(kombinacia))
                    time.sleep(float(speed))
                stop()
                quit()
            else:
                print("Choose the site")
                time.sleep(4)
                for kombinacia in kombinacie:
                    print(''.join(kombinacia))
                    pyautogui.typewrite(kombinacia)
                    pyautogui.press("enter")
                    time.sleep(float(speed))
                stop()
                quit()
                                
        else:
            print("\033[31mSorry virtual keyboard work only on desktop. Maybe sometimes this gonna work >:3\033[0m")
            time.sleep(4)
            for kombinacia in kombinacie:
                print(''.join(kombinacia))
                time.sleep(float(speed))
            stop()
            quit()

    def choosebruce():
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
            choosebruce()
    
    #Setting time
    timer_thread = threading.Thread(target=timecount, daemon=True)
    timer_thread.start()
    
    #Main controling System
    main()
    choosebruce()
except KeyboardInterrupt:
    stop()
    quit()