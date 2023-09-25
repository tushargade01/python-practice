class user():
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"{full_name}")
        print(f"\tUsername: {self.username}")
        print(f"\tEmail: {self.email}")
        print(f"\tLocation: {self.location}")

    def greet_user(self):
        print('Welcome back' + self.username + '!')   

    def incremnet_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0     

