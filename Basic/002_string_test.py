# 字符串函数实例
message = "I told you: 'Python is a good language'"
print(message)
print(message.title())
print(message.upper())
print(message.lower())

# f字符串 - Python 3.6引入
first_name = "Richie"
last_name ="zhu"
full_name = f"{first_name} {last_name}"
print(full_name.title())

# Python 3.6之前：format()
full_name = "{} {}".format(first_name, last_name)
print(full_name)


# 空白符：空格、制表符、换行符
print("Non Tab")
print("\t Has tab")
print("hello\nnew line")
print("Languages:\n\tPython\n\tC++\n\tGolang")


# 删除空白符
message = " python "
message = message.rstrip()
message = message.lstrip()
message = message.strip()




