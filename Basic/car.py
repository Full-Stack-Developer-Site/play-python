# 类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线
class Car:
    def __init__(self, make, model, yaar):
        self.make = make
        self.model = model
        self.year = yaar
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
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")
    
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    def __init__(self, make, model, yaar):
        super().__init__(make, model, yaar)
        self.battery = Battery()