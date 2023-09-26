import re
import getpass
import base64

def login(users_db):
    
    if len(users_db) == 0:
        print("No users db loaded, please register some users first.")
        return
    
    # Get the email
    while True:
        email = input("Please enter your registered email: ").strip().lower()
        
        if (email.lower() == "exit"):
            return 0
        
        if email.isspace() or len(email) == 0:
            print("Invalid input, email must not be empty, please try again or type exit to return to main menu")
            continue
        elif not(re.search('^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.[a-zA-Z]{2,3})+$', email)):
            print("Invalid email, please enter a valid one or type exit to return to main menu")
            continue
        elif email not in users_db:
            print("This email isn't registered before, please use another email or type exit to return to main menu")
            continue
        else:
            break
        
    user_data = users_db[email]
    tries = 3
    # Get the password
    while tries > 0:
        password = getpass.getpass()
        
        if (password.lower() == "exit"):
            return 0
        
        encoded_password = base64.b64encode(password.encode("utf-8")).decode("utf-8")
        
        if user_data.get("Password") == encoded_password:
            print(f'Hello {user_data.get("First_Name")} {user_data.get("Last_Name")}!')
            print("You've logged in successfully.")
            return email
        else:
            tries -= 1
            print("Wrong password, please re-enter your password or type exit if you want to return to main menu.")
            print(f"You've {tries} tries remaining.")
            continue
    return 0