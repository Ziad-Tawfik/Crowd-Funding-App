import re

def check_phone():
    while True:
        mobile = input("Please enter your mobile no.: ")
        mobreg = "^01[0125][0-9]{8}$"
        
        if (mobile.lower() == "exit"):
            return mobile
        
        if not re.search(mobreg, mobile):
            print("Invalid mobile no., please enter a valid Egyptian mobile number.")
            continue
        else:
            return mobile