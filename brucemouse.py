# Author: @patriq128

# Import libraries
import itertools
import string
import time
import threading
import os
import sys

# Import setup things
from setup import term, timecount, stop, device_type

# Setup tools
# ------------------------------------------------------
from Tools.keyboard_bruce import keyboard_bruce
from Tools.Custom_bruce.custom_bruce import custom_bruce
from Tools.calculate_bruce import calculate
from Tools.help_bruce import help_bruce
from Tools.config import config
# ------------------------------------------------------

try: 

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
2.) Custom Bruce
3.) Calculate Bruce
4.) Help
*) Config""")
        present = input("Select:")

        #Main Part
        if present == "1":
            keyboard_bruce()

        elif present == "2":
            custom_bruce()
        
        elif present == "3":
            calculate()
        
        elif present == "4":
            help_bruce()
        
        elif present == "*":
            config()
    
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
        elif "--cust" in sys.argv:
            custom_bruce()
        elif "--calc" in sys.argv:
            calculate()
        elif "--help" in sys.argv:
            help_bruce()
        elif "--conf" in sys.argv:
            config()
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
