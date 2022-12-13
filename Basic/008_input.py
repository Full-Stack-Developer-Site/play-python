# input
message = input('tell me: ')
print(f'you told me: {message}')


prompt = "this is a questions"
prompt += 'your name? : '
message = input(prompt)
print(f'your input: {message}')


# int()将数的字符串表示转换为数值表示
age = input('input your age: ')
age = int(age)
print(age > 10)


# 求模运输
number = input('enter a number: ')
number = int(number)
if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')

