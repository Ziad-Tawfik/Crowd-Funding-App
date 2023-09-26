import re
import datetime
from modules.write_users import write_projects

def edit_project(projects_db, email):
    while True:
        title = input(f"Please enter project title: ").strip()
        
        if (title.lower() == "exit"):
            return title
            
        if not (re.search('^[a-zA-Z]+[a-zA-Z0-9]*$', title)):
            print("Invalid input, title must not be empty or integers only, please try again or type exit to return to main menu")
            continue
        
        found = 0
        proj_idx = 0
        for index, proj in enumerate(projects_db[email]):
            if proj["Title"].lower() == title.lower():
                found = 1
                proj_idx = index
                print(f"Project {title} is found!")
                break
        else:
            print("No project found with this title, , please try again or type exit to return to main menu")
        
        if found: break  
        continue

    while True:
        print("1- Details")
        print("2- Target")
        print("3- Start Date & End Date")
        print("4- Exit")
        edit_col = input("Please choose which column you want to edit: ")
        
        if edit_col == '1':
            details = input(f"Please enter the project details: ").strip()
            projects_db[email][proj_idx]["Details"] = details
            write_projects(projects_db)
            
        elif edit_col == '2':
            while True:
                target = input(f"Please enter the project's total target (i.e. 250000 EGP): ").strip()
                
                if (target.lower() == "exit"):
                    return target
                    
                if not (re.search('^[0-9]+$', target)):
                    print("Invalid input, target must be integers only, please try again or type exit to return to main menu")
                    continue
                break
            projects_db[email][proj_idx]["Total_Target"] = target
            write_projects(projects_db)
            
        elif edit_col == '3':
            while True:
                start_date = input(f"Please enter the project's campaign start date (DD/MM/YYYY): ").strip()
                
                if (start_date.lower() == "exit"):
                    return start_date
                    
                if not (re.search('^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[1,2])\/(19|20)\d{2}$', start_date)):
                    print("Invalid input, start date must be date in this format (DD/MM/YYYY), please try again or type exit to return to main menu")
                    continue
                start_lst = start_date.split('/')
                start_date_var = datetime.date(int(start_lst[-1]), int(start_lst[1]), int(start_lst[0]))

                end_date = input(f"Please enter the project's campaign end date (DD/MM/YYYY): ").strip()
                
                if (end_date.lower() == "exit"):
                    return end_date
                    
                if not (re.search('^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[1,2])\/(19|20)\d{2}$', start_date)):
                    print("Invalid input, end date must be date in this format (DD/MM/YYYY), please try again or type exit to return to main menu")
                    continue
                
                end_lst = end_date.split('/')
                end_date_var = datetime.date(int(end_lst[-1]), int(end_lst[1]), int(end_lst[0]))
                
                t3 = end_date_var - start_date_var
                if t3.days <= 0:
                    print("End date cannot be before start date please enter a valid dates")
                    continue
                break
            projects_db[email][proj_idx]["Start_Date"] = start_date_var.strftime("%d/%m/%Y")
            projects_db[email][proj_idx]["End_Date"] = end_date_var.strftime("%d/%m/%Y")
            write_projects(projects_db)
            
        elif edit_col == '4':
            return 0
        else:
            print("Invalid input, please choose from above menu")  