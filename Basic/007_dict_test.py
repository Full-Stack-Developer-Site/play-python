# 字典 - 键值对
alien_0 = {'color':'green', 'points':5}
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])


# 添加键值对
# 在Python 3.7中，字典中元素的排列顺序与定义时相同。如果将字典打印出来或遍历其元素，将发现元素的排列顺序与添加顺序相同。
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


# 修改字典的值
alien_0['color'] = 'red'
print(alien_0)


# 删除键值对
del alien_0['color']
print(alien_0)


favorite_languages = {
    'jen' : 'python',
    'sarah' : "c",
    'Erwin' : 'ruby'
}

print(f'Sarah favorite language is {favorite_languages["sarah"]}')


# 使用get()访问值
# 如果指定的键有可能不存在，应考虑使用方法get()，而不要使用方括号表示法
sarah_favorite = favorite_languages.get('sarah', 'No sarah favorite language')
print(sarah_favorite)


# 字典遍历
user_0 = {
    'username' : 'richie',
    'first' : 'richie',
    'last' : 'zhu',
}

for key, value in user_0.items():
    print(f'\nkey: {key};  ')
    print(f'value: {value}; ')

# 遍历字典中的所有键
for key in user_0.keys():
    print(key)

for key in user_0:
    print(key)

# 遍历字典中的所有值
for language in favorite_languages.values():
    print(language.title())

# set集合
# 通过对包含重复元素的列表调用set()，可让Python找出列表中独一无二的元素
for language in set(favorite_languages.values()):
    print(language.title())

# 创建集合
# 不同于列表和字典，集合不会以特定的顺序存储元素
languages = {'python', 'python', 'Python'}
print(languages)


# 字典列表 - 列表中存储字典
aliens = []

for new in range(30):
    new_alien = {'color':'green', 'points': 5}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print(f'total number of alines: {len(aliens)}')

# 字典中存储列表
pizza = {
    'crust' : 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print(pizza)


# 在字典中存储字典

users = {
    'Cat' : {
        'first' : 'albert',
        'last' : 'en',
        'location' : 'shanghai'
    },
    'Jim' : {
        'first' : 'albert',
        'last' : 'en',
        'location' : 'shanghai'
    }
}
print(users)