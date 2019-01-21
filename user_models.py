users = {}

class User:
    """ class for creating a user"""
    def __init__(self, first_name, last_name, user_name, user_password,
                 user_time_stamp):
        self.user_id = len(users)+1
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.user_password = user_password
        self.user_type = "normal"

    def make_moderator(self):
        """ method makes a normal user a moderator"""
        self.user_type = "moderator"

    def make_admin(self):
        """ method makes a normal user an admin"""
        self.user_type = "admin"

    def to_json(self):
        """ Function returns user data in json format"""
        return {
                "user_id": self.user_id,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "user_name": self.user_name,
                "user_password": self.user_password,
                "user_type": self.user_type
                }
