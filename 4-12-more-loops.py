pizzas = ['cheese pizza','veggie pizza','meat pizza']
numbers = [1,2,3]
for value1,value2 in zip(pizzas,numbers):
  print(f'{value2}\t{value1}')