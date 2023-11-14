dictionary = dict(zip(['name', 'age', 'sex'], ['johannan', 69, 'nonstop']))

print(dictionary)

for key, value in dictionary.items():
    print(f"{key}:{value}")