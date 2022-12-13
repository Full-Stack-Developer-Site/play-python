import json

numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
with open(filename, 'w') as file_obj:
    json.dump(numbers, file_obj)


# 读取
with open(filename) as f:
    numbers = json.load(f)

print(numbers)