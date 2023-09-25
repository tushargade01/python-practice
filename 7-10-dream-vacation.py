data = {}
while True:
    name = input("What's your name? ")
    place = input('if you could visit one place in the world, where would it be? ')
    data[name] = place
    respond = input('\nWould you like to let someone else respond? (yes/no) ')
    if respond != 'yes':
        print('------Results------')
        for name,place in data.items():
            print(f"{name} would like to visit {place}")           