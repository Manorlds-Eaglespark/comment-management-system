from user import create_user, user_login


def main():
    """
    Allows user to create account and login
    """
    while True:
        print("1) Already have an accout, Please login.")
        print("2) Create account.")
        user_options = input("> ")
        if user_options == "1":
            if user_login() is True:
                print("Continue to the next step")
            else:
                return False
        elif user_options == "2":
            create_user("username", "password")

if __name__ == "__main__":
    main()
