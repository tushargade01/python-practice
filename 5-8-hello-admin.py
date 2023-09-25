usernames = ['tushar','rohan','rushi','karan','admin']
for user in usernames:
    if user == 'admin':
        print('Hello Admin, would you like to see a status report?')
    else:
        print(f'Hello {user.title()}, thank you for logging in again.')    