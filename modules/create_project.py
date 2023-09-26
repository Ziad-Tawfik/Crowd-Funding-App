import re
import datetime
from modules.write_users import write_projects

def create_project(projects_db, email):
    
    projects_db[email] = projects_db.get(email, [])
    
    while True:
        title = input(f"Please enter project title: ").strip()
        
        if (title.lower() == "exit"):
            return title
            
        if not (re.search('^[a-zA-Z]+[a-zA-Z0-9]*$', title)):
            print("Invalid input, title must not be empty or integers only, please try again or type exit to return to main menu")
            continue
        
        found = 0
        for proj in projects_db[email]:
            if proj["Title"].lower() == title.lower():
                found = 1
                print("There is another project with the same name, please enter another name or type exit to return to main menu")
                break
        if found: continue
        
        break
    
    details = input(f"Please enter the project details: ").strip()
    
    while True:
        target = input(f"Please enter the project's total target (i.e. 250000 EGP): ").strip()
        
        if (target.lower() == "exit"):
            return target
            
        if not (re.search('^[0-9]+$', target)):
            print("Invalid input, target must be integers only, please try again or type exit to return to main menu")
            continue
        break
    
    while True:
        start_date = input(f"Please enter the project's campaign start date (DD/MM/YYYY): ").strip()
        
        if (start_date.lower() == "exit"):
            return start_date
            
        if not (re.search('^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0,1,2])\/(19|20)\d{2}$', start_date)):
            print("Invalid input, start date must be date in this format (DD/MM/YYYY), please try again or type exit to return to main menu")
            continue
        start_lst = start_date.split('/')
        print(start_lst)
        start_date_var = datetime.date(int(start_lst[-1]), int(start_lst[1]), int(start_lst[0]))

        end_date = input(f"Please enter the project's campaign end date (DD/MM/YYYY): ").strip()
        
        if (end_date.lower() == "exit"):
            return end_date
            
        if not (re.search('^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[012])\/(19|20)\d{2}$', start_date)):
            print("Invalid input, end date must be date in this format (DD/MM/YYYY), please try again or type exit to return to main menu")
            continue
        
        end_lst = end_date.split('/')
        print(end_lst)
        end_date_var = datetime.date(int(end_lst[-1]), int(end_lst[1]), int(end_lst[0]))
        
        t3 = end_date_var - start_date_var
        if t3.days <= 0:
            print("End date cannot be before start date please enter a valid dates")
            continue
        
        break
    
    # Populate the dictionary with the new data
    projects_db[email] = projects_db.get(email, [])
    projects_db[email].append({})
    projects_db[email][-1]["Title"] = title
    projects_db[email][-1]["Details"] = details
    projects_db[email][-1]["Total_Target"] = target
    projects_db[email][-1]["Start_Date"] = start_date_var.strftime("%d/%m/%Y")
    projects_db[email][-1]["End_Date"] = end_date_var.strftime("%d/%m/%Y")
    
    # Write the new data
    write_projects(projects_db)