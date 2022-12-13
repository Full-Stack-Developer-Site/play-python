# Python使用称为异常的特殊对象来管理程序执行期间发生的错误。
# 每当发生让Python不知所措的错误时，它都会创建一个异常对象
# 异常是使用try-except代码块处理的。
# try-except代码块让Python执行指定的操作，同时告诉Python发生异常时怎么办

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


print('Give me two numbers, and I will divide them')
print("Enter 'q' to quit.")

while True:
    first_num = input("\n First Number:")

    if first_num == 'q':
        break
    second_num = input("Second number:")
    if second_num == 'q':
        break
    
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)


# FileNotFoundError
filename = 'alice.txt'

try:
    with open(filename, encoding='uft-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"\nSorry, the file {filename} does not exist")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")


# 静默失败 pass
try:
    print(5/0)
except ZeroDivisionError:
    pass