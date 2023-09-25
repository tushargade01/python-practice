prompt = True
while prompt:
    print('\nHow old are you?')
    age = input("Enter 'quit' when you are finished. ")
    if age == 'quit':
        prompt=False
    else:
        age = int(age)
        if age<=3:
            print('You get in free!')
        elif age>3 and age<=12:
            print('Your ticket is $10')
        elif age>12:
            print('Your ticket is $15')        