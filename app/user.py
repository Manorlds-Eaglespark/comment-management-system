users = {}

def create_user(username, password):
    """
    creates user
    """
    username = input("Please enter username: ")
    password = input("Please enter password: ")
    if username == "" or password == "":
        print("Fields can not be left empty.")
        return False
    if len(password ) < 5:
        print("Password too short, password shoul atleast be 6 characters.")
        return False
    if username in users.keys():
        print("Oopps! Username already taken.")
        print("Try a different username.")
        return False
    users[username] = password
    print("User successfully created. Please login to continue")
    return True

def user_login():
    """
    log in user
    """
    username = input("Please your username: ")
    password = input("Please your password: ")
    if username in users and users[username] == password:
        print("Successfully logged in.")
        return True
    else:
        print("Invalid credentials!")
        return False
