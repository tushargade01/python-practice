from random import choice

numbers_letters = ['A','B','C','D','E',0,1,2,3,4,5,6,7,8,9]
new_items = []
for num in range(1,5):
    new = choice(numbers_letters)
    new_items.append(new)
print(new_items)