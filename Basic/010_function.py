# 函数定义 def
# 文档字符串docstring 注释, Python使用它们来生成有关程序中函数的文档
def greet_user():
    """Show greet wording"""
    print('hello')

greet_user()



# 向函数传递信息
# 形参：函数定义时定义的参数变量
# 实参：函数调用时传递的信息
def greet_user(username, address = 'Earth'):
    """show greet wording by username"""
    print(f'hello {username}, your address is: {address}')

    return username.title()

greet_user("Cat", "Shanghai")
greet_user(username='Cat', address='Shanghai')
return_username = greet_user('Cat')
print(f'username is: {return_username}')



# None占位值
def build_person(first_name, last_name, age = None):
    person = {'first': first_name, 'last':last_name}
    if age:
        person['age'] = age
    
    return person

jerry = build_person('jerry', 'hong', age=27)
print(jerry)



# 传递列表
def greet_names(usernames):
    for name in usernames:
        msg = f'hello {name}'
        print(msg)

names = ['cat', 'jerry', 'paul']
greet_names(names)

# 将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的
# 如果避免修改list，可以将列表的副本传递给函数 e.g. 不清空unprinted_designs： print_models(unprinted_designs[:], completed_models)
# 切片表示法[:]创建列表的副本
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，打印后，都将其移到complete列表中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing model: {current_design}')
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print('\n The following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# 传递任意数量的实参 - 一个星号
# 形参名*toppings中的星号让Python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中
# 任意数量实参的形参放在最后
def make_pizza(size, *toppings):
    """打印顾客点的所有配料"""
    print(toppings)

make_pizza(16, 'pepperoni')
make_pizza(20, 'mushrooms', 'green peppers', 'extra cheese')

# 任意数量的关键字实参 - 接收任意数量的键值对
# 形参两个星号 - 形参**user_info中的两个星号让Python创建一个名为user_info的空字典
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

user_profile = build_profile('Jerry', "Hu", location='shanghai', filed='physics')
print(user_profile)


# import module
# 注： 所有import语句都应放在文件开头。唯一例外的情形是，在文件开头使用了注释来描述整个程序。
import pizza
pizza.make_your_pizza(16, 'mushrooms', 'green peppers')

# 导入特定的函数
from pizza import make_your_pizza
make_your_pizza(16, 'mushrooms', 'green peppers')

# 函数别名
from pizza import make_your_pizza as mp
mp(16, 'mushrooms', 'green peppers')

# module别名
import pizza as p
p.make_your_pizza(16, 'mushrooms', 'green peppers')

# 导入模块中的所有函数
# 注： 最佳的做法是，要么只导入需要使用的函数，要么导入整个模块并使用句点表示法。这让代码更清晰，更容易阅读和理解
from pizza import *
make_your_pizza(16, 'mushrooms', 'green peppers')