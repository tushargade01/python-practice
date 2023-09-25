glassary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the python interpeter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': 'A collection of key-value pairs.'
}
print(glassary)#print glassary as default
for key, value in glassary.items():
    print(f'{key}:\n{value}\n')