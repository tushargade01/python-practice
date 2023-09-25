friend_pizzas = ['cheese','veggie','meat']
my_favorite = friend_pizzas[:]
print(my_favorite) 
print('\n')
print("Add new pizza in orignal list:")
my_favorite.append('maegherita')
print(my_favorite)

print("\nAdd new pizza in friend pizza:")
friend_pizzas.append('pepperoni')
print(friend_pizzas)

print('\n')

for pizza in my_favorite:
  print(f'My favorite pizzas are: {pizza}')
print('\n')
for pizza in friend_pizzas:
  print(f"My friend's favorite pizzas are: {pizza}")  