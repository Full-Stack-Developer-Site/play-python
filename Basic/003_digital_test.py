# 浮点数 - 结果包含的小数位数可能是不确定的
result = 0.1 + 0.2
print(result)

result = 0.2 + 0.2
print(result)

# 任意两个数相除时，结果总是浮点数
result = 4 / 2
print(result)

# 数中的下划线 - 书写很大的数时使用
# 适用于整数和浮点数
# Python version >= 3.6
result = 140_000_000
print(result)

print(12.589_333)


# 同时给多个变量赋值
x, y, z = 3, 4, 5
print(x, y, z)


# Python没有内置的常量类型，但Python程序员会使用全大写来指出应将某个变量视为常量
MAX_CONNECTIONS = 500
print(MAX_CONNECTIONS)


# Python 之禅 - 在Python终端会话中执行命令import this
# The Zen of Python, by Tim Peters
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!