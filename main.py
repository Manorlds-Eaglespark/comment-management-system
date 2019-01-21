import datetime
from user_models import User, users

def run_app():
    welcome = """
    Welcome to my app.
    What do you want to do?
    1.Register
    2.Login
    3.Create comment
    """
    print(welcome)

    text = input("Enter a number:")

    if text == 1:
        register_user()
    elif text == 2:
        login_user()
    elif text == 3:
        create_comment()
    else:
        print("I'm sorry, I don't get you.")

def register_user():
    print("\nPlease register here.")
    username = raw_input("Username:")
    password = raw_input("Password:")
    firstname = raw_input("Firstname:")
    last_name = raw_input("Last name:")
    user = User(firstname, last_name, username, password)
    users[user.id] = user
    print("Welcome {}, your id is {}".format(username, user.id))
    login_user()

def login_user():
    print("\nPlease log in.")
    username = raw_input("Username:")
    password = raw_input("Password:")
    print("Welcome {}, your password is {}".format(username, password))
    run_app()

def create_comment():
    print("\nCreate a comment here.")
    username = raw_input("Username:")
    message = raw_input("Enter your comment:")
    timestamp = datetime.datetime.now()

    print("Hello {}, your comment with message {} has been successfully created at {}".format(username, message, timestamp))

if __name__ == '__main__':
    run_app()