import re
from modules.write_users import write_projects

def delete_project(projects_db, email):
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
    
    del projects_db[email][proj_idx]
    write_projects(projects_db)