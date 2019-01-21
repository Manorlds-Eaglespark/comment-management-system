users = {}

class User:
    """ class for creating a user"""
    def __init__(self, first_name, last_name, user_name, user_password):
        self.id = len(users)+1
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.user_password = user_password
        self.user_type = "normal"
        self.last_logged_in = None

    def last_logged_in(self, time):
        self.last_logged_in = time

    def make_admin(self):
        self.user_type = 'admin'

    def make_moderator(self):
        self.user_type = 'moderator'

    def to_json(self):
        """ Function returns user data in json format"""
        return {
                "id": self.id,  
                "first_name": self.first_name,
                "last_name": self.last_name,
                "user_name": self.user_name,
                "user_password": self.user_password,
                "user_type": self.user_type,
                }

    @staticmethod
    def check_user(username):
        if username in users:
            return True
        else:
            return False