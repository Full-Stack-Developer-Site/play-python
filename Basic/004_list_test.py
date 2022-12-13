program_language = ["C", "Java", "Python", ".Net", 1, 5 + 3.2]
print(program_language)

# 访问元素
print(program_language[0])
print(program_language[-1])

# f字符串 + list
messagge = f"my love: {program_language[2].title()}"
print(messagge)

# 修改元素
program_language[4] = "Sehll"
print(program_language)

# list末尾添加元素
program_language.append("C++")
print(program_language)

# list中插入元素
program_language.insert(0, "Javascript")
print(program_language)

# list删除元素
del program_language[5]
print(program_language)

# pop删除list末尾元素，并可使用它
pop = program_language.pop()
print(program_language)
print(f"pop element: {pop}")

# pop list中任意位置元素
pop = program_language.pop(5)
print(program_language)
print(f"pop element: {pop}")

# 如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用del语句；
# 如果你要在删除元素后还能继续使用它，就使用方法pop()。


# remove() - 根据值删除元素
program_language.remove("C")
print(program_language)



# sort() - 对list永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse= True)
print(cars)


# sorted() - 对list临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(sorted(cars, reverse=True))
print(cars)

# reverse() - 永久倒置list
cars.reverse()
print(cars)


# len() - list长度
print(len(cars))
