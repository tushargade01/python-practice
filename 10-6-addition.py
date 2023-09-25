num_1 = input("Give me a number: ")
num_2 = input("Give me a another number: ")

try:
    result = int(num_1) + int(num_2)
except ValueError:
      print("Sorry, I really needed a number.")    
else:
    print(f"The sum of {num_1} and {num_2} is {result}.")