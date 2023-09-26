from modules.write_users import write_users 
from modules.check_user import check_user
from modules.check_email import check_email
from modules.check_pass import check_pass
from modules.check_phone import check_phone


# Function to register a new user
def register(users_db):
    # Get the first name
    fname = check_user("Please enter your first name: ")
    if fname == "exit" : return
    
    # Get the last name
    lname = check_user("Please enter your last name: ")
    if lname == "exit" : return
    
    # Get the email
    email = check_email(users_db)
    if email == "exit" : return
    
    # Get the password
    encoded_password = check_pass()
    if encoded_password == "exit" : return
    
    # Get the mobile number
    mobile = check_phone()
    if mobile == "exit" : return

    # Populate the dictionary with the new data
    users_db[email] = {}
    users_db[email]["First_Name"] = fname
    users_db[email]["Last_Name"] = lname
    users_db[email]["Password"] = encoded_password.decode("utf-8")
    users_db[email]["Mobile_No."] = mobile
    
    # Write the new data
    write_users(users_db)