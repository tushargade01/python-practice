class restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name 
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.increment = 0

    def describe_restarurant(self):
        print(f"The {self.name} serves wonderful {self.cuisine_type}.")
        
    def open_restaurant(self):
        print(f"the {self.name} open. come on in!")  

    def set_number_served(self,number_served):
        self.number_served = number_served

    def increment_number_served(self):
        self.increment += 1   

class IceCreamStand(restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print('we have the following flavors available: ')
        for flavor in self.flavors:
            print(f"-{flavor}")
            
    def describe_stand(self):
        print(f"The {self.name.title()} serves wonderful {self.cuisine_type.title()}.")

my_restaurant = IceCreamStand('Tushar ice cream stand', 'Ice Cream')
my_restaurant.flavors = ['vailla', ' chocolate']

my_restaurant.describe_stand()
my_restaurant.display_flavors()
