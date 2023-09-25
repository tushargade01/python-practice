def send_messages(names):
    while names:
            new_user = names.pop()
            print(new_user)
            new_users.append(new_user) #add value to new user list


users = ['tushar','shubham','vinod']    
new_users = []
send_messages(users)
for user in new_users:
    print(f'hello , {user}')