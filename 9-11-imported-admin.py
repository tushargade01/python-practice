import Userpadmin as user
user_info = user.admin('tushar','gade','tushargade_01','tushargade205@gmail.com','karjat')

user_info.describe_user()

details = [
    'can reset passwords',
    'can moderate discussiions',
    'can suspend accounts'
]

user.Privilege(details).show_peivileges()