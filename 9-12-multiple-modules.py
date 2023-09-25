import User
import Priadmin

user_info = User.user('tushar','gade','tushargade_01','tushargade205@gmail.com','karjat')

user_info.describe_user()

details = [
    'can reset passwords',
    'can moderate discussiions',
    'can suspend accounts'
]

Priadmin.Privilege(details).show_peivileges()