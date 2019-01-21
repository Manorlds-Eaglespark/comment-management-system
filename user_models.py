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


    def to_json(self):
        """ Function returns user data in json format"""
        return {
                "id": self.id,  
                "first_name": self.first_name,
                "last_name": self.last_name,
                "user_name": self.user_name,
                "user_password": self.user_password,
                "user_type": self.user_type,
                "user_time_stamp": self.user_time_stamp
                }