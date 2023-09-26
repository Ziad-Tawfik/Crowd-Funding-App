"""Crowd-Funding console app"""
import os
import sys
import modules as m
import Project as p

def main():
    while True:
        choice = input("Please enter your choice from above menu: ")
        
        if (choice.lower() == "exit"):
            exit()
        
        if choice == '1':
            m.register(users_db)
            break
        elif choice == '2':
            loginemail = m.login(users_db)
            
            if loginemail != 0 : p.start(loginemail)
            else: break
        else:
            print("Invalid input, please choose either 1 or 2 or type exit to break")     

if __name__ == "__main__":
    
    if 'linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')
        
    while True:
        users_db = m.load_users()
        
        if len(users_db) == 0:
            print("No users exist in current DB, please register some users first.")
            
        print("\n\n### Crowd-Funding Application ###")
        print("1- Register new user")
        print("2- Login")
        main()