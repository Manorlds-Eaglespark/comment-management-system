import datetime
from app.user_models import User, users
from app.user import create_user, user_login
from app.comment import create_comment

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
    create_user()
    login_user()

def login_user():
    print("\nPlease log in.")
    user_login()
    create_comment()

if __name__ == '__main__':
    run_app()