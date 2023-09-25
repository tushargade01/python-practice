class restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name 
        self.cuisine_type = cuisine_type

    def describe_restarurant(self):
        print(f"The {self.name} serves wonderful {self.cuisine_type}.")
        
    def open_restaurant(self):
        print(f"the {self.name} open. come on in!")  


my_restaurant = restaurant('The Tushar Restaurant', 'pizza')
print(my_restaurant.name)  
print(my_restaurant.cuisine_type)          
my_restaurant.open_restaurant()
my_restaurant.describe_restarurant()