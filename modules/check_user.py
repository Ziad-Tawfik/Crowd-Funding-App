import re

def check_user(message="Please enter your name: "):
    while True:
        name = input(f"{message}").strip()
        
        if (name.lower() == "exit"):
            return name
            
        if not (re.search('^[a-zA-Z]+$', name)):
            print("Invalid input, name must not be empty or integers, please try again or type exit to return to main menu")
            continue
        return name