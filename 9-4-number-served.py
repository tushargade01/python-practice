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


my_restaurant = restaurant('Tushar Restaurant', 'pizza')
print(f"Number served : {my_restaurant.number_served}")

my_restaurant.number_served = 40
print(f"Number served : {my_restaurant.number_served}")

my_restaurant.set_number_served(60)
print(f"Number served : {my_restaurant.number_served}")

my_restaurant.increment_number_served() #increment = increment + 1
print(f'increment is : {my_restaurant.increment}')

my_restaurant.increment_number_served() #increment = increment + 1

my_restaurant.increment_number_served() #increment = increment + 1

print(f'increment is : {my_restaurant.increment}')