import datetime
import re
from tabulate import tabulate

def find_project(projects_db):
    found_projects = {}
    
    while True:
        search_date = input(f"Please enter the search date for project's campaign (DD/MM/YYYY): ").strip()
        
        if (search_date.lower() == "exit"):
            return search_date
            
        if not (re.search('^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0,1,2])\/(19|20)\d{2}$', search_date)):
            print("Invalid input, start date must be date in this format (DD/MM/YYYY), please try again or type exit to return to main menu")
            continue
        search_lst = search_date.split('/')
        search_date_var = datetime.datetime(int(search_lst[-1]), int(search_lst[1]), int(search_lst[0]))
        break
    
    for email, proj_lst in projects_db.items():
        for proj in proj_lst:
            start_date_var = datetime.datetime.strptime(proj["Start_Date"], "%d/%m/%Y")
            end_date_var = datetime.datetime.strptime(proj["End_Date"], "%d/%m/%Y")
            
            if search_date_var >= start_date_var and search_date_var <= end_date_var:
                found_projects[email] = found_projects.get(email, [])
                found_projects[email].append(proj)
            else:
                continue

    if len(found_projects) == 0:
        print("No projects found with that date")
        return
    else:
        headers = ["Email", "Projects"]
        print(tabulate(found_projects.items(), headers=headers))
        return
            
    