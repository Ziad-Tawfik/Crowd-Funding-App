import re
import getpass
import base64

def check_pass():
    while True:
        password = getpass.getpass()
        passreg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$"
        
        if (password.lower() == "exit"):
            return password
        
        if not re.search(passreg, password):
            print("Sorry password doesn't match the below criteria:")
            print("\tShould have at least one number.")
            print("\tShould have at least one uppercase and one lowercase character.")
            print("\tShould have at least one special symbol.")
            print("\tShould be minimum 8 characters long.")
            print("\tType exit if you want to return to main menu.")
            continue
        
        conf_password = getpass.getpass(prompt="Confirm Password: ")
        if conf_password != password:
            print("Both passwords don't match, please try again")
            continue
        elif conf_password == password:
            encoded_password = base64.b64encode(password.encode("utf-8"))
            return encoded_password