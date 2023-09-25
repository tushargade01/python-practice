# this file is used to 8-16-imports.py for importing the sandwiches function

def sandwichs(*toppings):
    print("\nI'll make you a great sandwich:")
    for topping in toppings:
        print(f'....adding {topping.title()} to your sandwich.')
    print('Your sandwich is ready!\n')    