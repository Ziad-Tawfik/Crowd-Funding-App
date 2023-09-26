from tabulate import tabulate
from modules.load_users import load_projects

def view_projects():
    projects_db = load_projects()
    if len(projects_db) == 0:
        print("Empty Projects DB, please insert some data")
    else:
        proj_tab = []
        headers = ["Email", "Title", "Details", "Total_Target", "Start_Date", "End_Date"]
        # print(tabulate([(k,) + (v.values) for k,v in projects_db.items()], headers=headers))
        for email, proj_lst in projects_db.items():
            for proj in proj_lst:
                proj_tab.append((email,) + tuple(proj.values()))
        
        print(tabulate(proj_tab,headers=headers))