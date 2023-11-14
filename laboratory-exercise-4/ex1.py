dictionary = {
    'age1': 0,
    'age2': 0,
    'age3': 1
}

max_age = 0
max_name = ''

for key, value in dictionary.items():
    if value > max_age:
        max_age = value
        max_name = key


print(f'{max_name}:{max_age}')