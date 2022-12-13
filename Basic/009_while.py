cur = 1
while cur <= 5:
    print(cur)
    cur += 1

# while退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program: \n"

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(f'your input: {message}')


# 使用标志 flag
active = True
while active:
    message = input("pls your input:")

    if message == 'quit':
        active = False
    else:
        print(message)


# break退出
while True:
    city = input('input the city:')

    if city == 'quit':
        break
    else:
        print(f'love the city: {city}')


# continue 退出当前循环，继续下一循环
cur = 1
while cur < 10:
    if cur % 2 == 0:
        cur += 1
        continue
    
    print(cur)
    cur += 1

# 删除为特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'fish', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)