from setup import timecount, stop

def help_bruce():
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