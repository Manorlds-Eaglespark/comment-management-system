from app.user_models import users
import datetime
from app.user_models import User

comments = {}

class Comments:
   def __init__(self,author,message,timestamp):
      self.comment_id = len(comments)+1
      self.author = author
      self.message = message
      self.timestamp = timestamp
      
   def to_json(self):
      return {
               "comment_id": self.comment_id,
               "author":self.author,
               "message":self.message,
               "timestamp":self.timestamp
            }

   def add_comment(self, author):
      if User.check_user(author):
         comments[self.comment_id] = self
         return "Succesfull created comment with id = {}".format(self.comment_id)
      else:
         return "User doesn't exist."

def create_comment():
    print("\nCreate a comment here.")
    username = raw_input("Username:")
    message = raw_input("Enter your comment:")
    timestamp = datetime.datetime.now()
    comment = Comments(username, message, timestamp)
    print(comment.add_comment(username))
