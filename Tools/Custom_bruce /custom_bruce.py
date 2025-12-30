# Author: @patriq128

import itertools
import string
import time
import json

from setup import term, timecount, stop, device_type

def custom_bruce():
    print("\033[2J\033[H", end="")
    print("""\033[32m Custom Bruce \033[0m""") # !Dont forget change NAME!
    print("\033[0m---------------------------------------------------------------------------------------------------------")
    print("""a) Show save files
b) Run save files
c) New file""")

def custom_program():
    print("nothing")
