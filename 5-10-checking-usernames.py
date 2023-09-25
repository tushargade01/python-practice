current_usernames = ['tushar','rohan','rushi','karan','shubham','sandip','vishal','admin']
new_users = ['tushar','krushna','rushi','sujal','vinod']
for users in new_users:
    if users in current_usernames:
        print('the person will need to enter a new username.')
    elif users not in current_usernames: #is not menas != 
        print('the username is available.')    
