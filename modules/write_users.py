import json

# Function to write users to the json file
def write_users(users_db):
    try:
        with open('data/users.json', 'w') as file:
            json.dump(users_db, file, indent=4)
            print("### Updating Users DB Completed ###")
            return
    except Exception as e:
        print(f"Couldn't update the database file due to exception: {e}")
        return

# Function to write projects to the json file
def write_projects(projects_db):
    try:
        with open('data/projects.json', 'w') as file:
            json.dump(projects_db, file, indent=4)
            print("### Updating Projects DB Completed ###")
            return
    except Exception as e:
        print(f"Couldn't update the database file due to exception: {e}")
        return