names = ['tushar','sandip','vishal','anand']

for i in names:
    if i == 'tushar':
        print('it is found')      
    if i.upper() != 'snadip':
        print('sandip not found')    

age = 50
if age >= 18 and age<= 25:
    print('you are 18+')
elif age>25 and age<50:
    print('age is greater than 25 and lessthan 50')    
elif age <= 50:
    print('your are less than or equal to 50')                 

print('\n')

friuts = 'mango'

if 'mango' in friuts:
    print('it is in the list.')
if 'apple' is not friuts:
    print('it not found')    