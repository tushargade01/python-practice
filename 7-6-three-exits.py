while True:
    print('\nWhat topping would you like on your pizza?')
    pizza = input("Enter 'quit' when you are finished: ")
    if pizza == 'quit':
        break
    else:
        print(f"I'll add {pizza.title()} to your pizzza.")    