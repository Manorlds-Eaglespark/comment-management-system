from user_models import User

users = {}

def create_user():
    """
    creates user
    """
    print("\nPlease register here.")
    username = raw_input("Username:")
    password = raw_input("Password:")
    firstname = raw_input("Firstname:")
    last_name = raw_input("Last name:")
    user = User(firstname, last_name, username, password)
    users[user.user_name] = user
    print("Welcome {}, your id is {}".format(username, user.id))

def user_login():
    """
    log in user
    """
    username = raw_input("Enter username: ")
    password = raw_input("Enter password: ")
    if username in users and users[username].user_password == password:
        print("Successfully logged in.")
    else:
        print("Invalid credentials!")
        user_login()

