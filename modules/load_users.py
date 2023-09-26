import json

# Function to load json file for users
def load_users():
    try:
        with open('data/users.json', 'r') as file:
            users_db = json.load(file)
            return users_db
    except:
        users_db = {}
        return users_db
    finally:
        print("### Loading Users DB Completed ###")
        
# Function to load json file for projects
def load_projects():
    try:
        with open('data/projects.json', 'r') as file:
            projects_db = json.load(file)
            return projects_db
    except:
        projects_db = {}
        return projects_db
    finally:
        print("### Loading Projects DB Completed ###")