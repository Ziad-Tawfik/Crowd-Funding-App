import re

def check_email(users_db, message="Please enter your email: "):
    while True:
        email = input("Please enter your email: ").strip().lower()
        
        if (email.lower() == "exit"):
            return email
        
        if email.isspace() or len(email) == 0:
            print("Invalid input, email must not be empty, please try again or type exit to return to main menu")
            continue
        elif not(re.search('^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.[a-zA-Z]{2,3})+$', email)):
            print("Invalid email, please enter a valid one or type exit to return to main menu")
            continue
        elif email in users_db:
            print("This email is already registered before, please use another email")
            continue
        else:
            return email