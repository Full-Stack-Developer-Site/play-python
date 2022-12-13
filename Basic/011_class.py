# 根据约定，在Python中，首字母大写的名称指的是类
# 形参self必不可少，而且必须位于其他形参的前面
# 以self为前缀的变量可供类中的所有方法使用
# 为何必须在方法定义中包含形参self呢？因为Python调用这个方法来创建Dog实例时，将自动传入实参self。
# 每个与实例相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法
class Dog:
    """Dog 类描述"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f'{self.name} is now sitting')
    
    def roll_over(self):
        print(f'{self.name} rolled over')


# 创建类实例
my_dog = Dog("Cat", 6)
print(f'My dog name is {my_dog.name}')
print(f"My dog is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()

# 修改属性
my_dog.age = 10
print(my_dog.age)

# 类继承
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        desc_name = f"{self.year} {self.make} {self.model}"
        return desc_name.title()
    
    def read_odometer(self):
        print(f"this car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading + miles

    def fill_gas_tank(self):
        print("This care need a gas rank")

# 定义子类时，必须在圆括号内指定父类的名称。方法__init__()接受创建Car实例所需的信息
# super()是一个特殊函数，让你能够调用父类的方法
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        print("This car does not need a gas rank!")


my_tesla = ElectricCar('tesla', 'model s', 2022)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


# 重写父类方法
my_normal_car = Car('xue', 'middle', 2017)
my_normal_car.fill_gas_tank()
my_tesla.fill_gas_tank()
