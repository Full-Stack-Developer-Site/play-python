# 从一个模块中导入多个类
from car import Car, ElectricCar

my_car = Car('audi', 'a4', 2019)
print(my_car.get_descriptive_name())

my_car.odometer_reading = 23
my_car.read_odometer()


my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
