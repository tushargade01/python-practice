
class admin():
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0

class Privilege():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_peivileges(self):
        print('privileges :'.title())
        print(f"{self.privileges}")
        if self.privileges:
          for privilege in self.privileges:    
             print(f"- {privilege}")
        else:
            print("privilege is not found")     
