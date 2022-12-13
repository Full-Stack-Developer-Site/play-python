cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# and , or
age_1 = 22
age_2 = 18

if (age_1 > 20) and (age_2 < 10):
    print('ooh..')
else:
    print('oooo')

if (age_1 > 20) or (age_2 < 10):
    print('ooh..')
else:
    print('oooo')


# 检查特定值是否包含在列表中 - 不包含在list中
languages = ['C', 'C++', 'Python']

print('C' in languages)
print('C' not in languages)
print('Java' in languages)
print('Java' not in languages)


# if-elif-else
age = 10
if age < 10:
    print('age < 10')
elif age > 100:
    print('age > 100')
else:
    print('right age')


# 确定list是否为空
names = []

if names:
    print(f'names has {len(names)} emlements')
else:
    print(f'names is empty')
