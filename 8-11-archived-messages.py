def show_message(users):
    while users:
       poped_user = users.pop()
       print(poped_user)
       new_person.append(poped_user)

person = ['tushar','shubham','vinod']
new_person = []
show_message(person[:])
person.reverse()
print(f'original list after poping: {person}')
for new in new_person:
    print(f'Hello, "{new.title()}"')