# 读取整个文件
# 关键字with在不再需要访问文件后将其关闭
# 该输出唯一不同的地方是末尾多了一个空行。
# 为何会多出这个空行呢？因为read()到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行
# 要删除多出来的空行，可在函数调用print()中使用rstrip()
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    
print(contents.rstrip())

print('')

# 逐行读取
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())


print('')


# 创建一个包含文件各行内容的列表

filename = "pi_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))


# 写入文件
# 打开文件时，可指定读取模式（'r'）、写入模式（'w'）、附加模式（'a'）或读写模式（'r+'）。
# 如果省略了模式实参，Python将以默认的只读模式打开文件。
filename = "test_write.txt"
with open(filename, 'w') as file_obj:
    file_obj.write("I love programming")

# 以写入模式（'w'）打开文件时千万要小心，因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件的内容
with open(filename, 'w') as file_obj:
    print(f'check {filename} whether it is empty')

# Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式。
with open(filename, 'r+') as file_obj:
    file_obj.write(str(100))


# 写入多行
# 函数write()不会在写入的文本末尾添加换行符
filename = 'programming.txt'

with open(filename, 'w') as file_obj:
    file_obj.write('I love programming\n')
    file_obj.write('I love creating new games\n')



# 附加到文件
# 如果要给文件添加内容，而不是覆盖原有的内容，可以以附加模式打开文件。
# 以附加模式打开文件时，Python不会在返回文件对象前清空文件的内容，而是将写入文件的行添加到文件末尾
with open(filename, 'a') as file_obj:
    file_obj.write('I also love finding meaning in large database \n')
