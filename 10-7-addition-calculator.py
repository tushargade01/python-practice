print("Enter 'quit' or 'q' for exit the program.")

while True:
     num_1 = input("\nGive me a number: ")
     if num_1=='quit' or num_1=='q':
        break
     num_2 = input("Give me a another number: ")
     if num_1=='quit' or num_1=='q':
        break
     try:
        result = int(num_1) + int(num_2)
     except ValueError:
           print("Sorry, I really needed a number.")     
     else:
        print(f"The sum of {num_1} and {num_2} is {result}.")   