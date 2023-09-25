pets = []
pet = {
    'weight': 2,
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'eats': 'seeds'
}
pets.append(pet)

pet = {
    'weight': 43,
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'eats': 'bugs'
}
pets.append(pet)

pet = {
    'weight': 37,
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'eats': 'shoes'
}
pets.append(pet)
print(pets)
for data in pets:
    print(f"\nHere's what I konw about {data['name']}")
    for key,value in data.items():
        print(f'{key} {value}')
