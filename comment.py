comment_db = []

class Comments:
     def __init__(self,author,message,timestamp):
      self.comment_id = len(comment_db)+1
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

     def add_comment(self):
         comment_db.append(to_json())


 
 
     def edit_comment(self):

 
 
 
    def delete_comment(self):


    def add_reply(self):
