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


user_info = user('tushar','gade','tushargade_01','tushargade205@gmail.com','karjat')

user_info.describe_user() 
user_info.greet_user()

print('\n')

user_info.incremnet_login_attempts()
user_info.incremnet_login_attempts()
user_info.incremnet_login_attempts()
print(f'increment: {user_info.login_attempts}') # it increment three time in upper lines   

user_info.reset_login_attempts()
print(f'login attempts: {user_info.login_attempts}')

user_info.incremnet_login_attempts()
print(f'increment: {user_info.login_attempts}') #after reset login attempt it increment by 1

#user_info_1 = user('anand','adhav','mr_andy_adhav','anandadhav56@gmail.com','karjat')

#user_info_1.describe_user()
#user_info_1.greet_user()
