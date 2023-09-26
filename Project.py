"""Projects main menu console app"""
import os
import sys
import modules as m

def main(projects_db, email):
    while True:
        choice = input("Please enter your choice from above menu: ")
        
        if choice == '1':
            m.create_project(projects_db, email)
            break
        elif choice == '2':
            m.view_projects()
            break
        elif choice == '3':
            m.edit_project(projects_db, email)
            break
        elif choice == '4':
            m.delete_project(projects_db, email)
            break
        elif choice == '5':
            m.find_project(projects_db)
            break
        elif choice == '6':
            return 0
        else:
            print("Invalid input, please choose from above menu")     


def start(email):
    if 'linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')
        
    while True:
        projects_db = m.load_projects()
        
        print("\n\n### Projects Main Menu ###")
        print("1- Create a new project")
        print("2- View all projects")
        print("3- Edit a project")
        print("4- Delete a project")
        print("5- Search for a project using date")
        print("6- Exit")
        
        main_fb = main(projects_db, email)
        if main_fb == 0: return
        