from random import randint

class Die():
    def __init__(self, default_value = 6):
        self.default_value = default_value

    def roll_die(self):
        for number in range(1,11):
            print(f"{number} : {randint(1,self.default_value)}") 
print('\nFor 6 sided :')
Die().roll_die()       
print('\nFor 10 sided :')
Die(10).roll_die()
print('\nFor 20 sided :')
Die(20).roll_die()