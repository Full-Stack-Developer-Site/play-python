cars = ['bmw', 'audi', 'toyota', 'subaru']

for car in cars:
    print(car)
    print(f'{car.title()} is great!\n')

# 不会报错
print(car)


# range()
for value in range(1, 5):
    print(value)

for value in range(5):
    print(value)


# 使用range()创建数字list
numbers = list(range(1,5))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1,5):
    squares.append(value ** 2)
print(squares)

# 数字列表统计
digits = range(0,11)
print(f'min value: {min(digits)}')
print(f'max value: {max(digits)}')
print(f'sum: {sum(digits)}')

# 列表解析
squares = [value ** 2 for value in range(1,10)]
print(squares)

# list切片
players = ['charles', 'Jerry', 'Cat', 'Eli']
print(players[0:3])
print(players[2:4])
print(players[:4])
print(players[1:])
print(players[::2])

# 遍历切片
for player in players[0:3]:
    print(player)


# 复制list - 得使用切片方式，不可直接赋值
new_players = players[:]
same_players = players
players.append("new")

print(players)
print(new_players)
print(same_players)


# 列表是可以修改的
# tuple - 元组 - Python将不能修改的值称为不可变的，而不可变的列表被称为元组
# 如果需要存储的一组值在程序的整个生命周期内都不变，就可以使用元组
dimentions = (2, 5, 8)
print(dimentions)

one_tuple = (3,)
print(one_tuple)

