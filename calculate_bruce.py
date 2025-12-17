import string

from setup import timecount, stop

def calculate():
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