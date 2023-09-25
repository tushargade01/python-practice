class restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name 
        self.cuisine_type = cuisine_type

    def describe_restarurant(self):
        print(f"\nThe {self.name} serves wonderful {self.cuisine_type}.")
        
    def open_restaurant(self):
        print(f"the {self.name} open. come on in!")  


my_restaurant = restaurant('The Tushar Restaurant', 'pizza')
my_restaurant.describe_restarurant()

my_restaurant = restaurant('The Anand Restaurant', 'seafood')
my_restaurant.describe_restarurant()

my_restaurant = restaurant('The Shubham Restaurant', 'thai')
my_restaurant.describe_restarurant()