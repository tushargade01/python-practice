class Car:
     def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

     def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

     def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

     def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back an odometer!")

     def increment_odometer(self, miles):
        self.odometer_reading += miles 

class battery():
    def __init__(self, battery_size = 60):
        self.battery_size = battery_size

    def upgrade_battery(self):
        if self.battery_size == 60:
            self.battery_size = 85
            print(f"Upgraded the battery to {self.battery_size} kWh.")
        else:
            print("The battery is already upgraded.")    
    def get_range(self):
            if self.battery_size == 60:
                range = 140
            elif self.battery_size == 80:
                range = 185  
            print(range)   
            
class ElectricCar(Car):
     def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())                              

battery(60).upgrade_battery()
# battery().get_range()
battery(60).get_range()  
