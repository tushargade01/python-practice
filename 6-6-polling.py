people = {
    'jen': 'python',
    'sarah': 'c',
    'phil': 'python',
    'edward': 'ruby',
    'sachin': 'javascript',
}
new_user = {
    'jen': 'python',
    'sarah': 'c',
    'phil': 'python',
    'balaji': 'dotnet',
    'edward': 'ruby',
    'sachin': 'javascript',
    'abujar': 'Java'    
}
for key,value in people.items():
    print(f"{key.title()}'s favorite language is {value.title()}")
print('\n')    
for keys in new_user.keys():
    if keys not in people:
        print(f"{keys}, what's your favorite prgramming language?")
    else:
        print(f'Thanks you for taking the poll, {keys}!') 