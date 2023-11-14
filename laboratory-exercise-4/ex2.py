list_name = []

size_name = int(input('set size'))

for name in range(size_name):
    name = input('set name:')
    list_name.append(name)

list_age = []

size_age = size_name

for age in range(size_age):
    age = int(input('set age:'))
    list_age.append(age)

dictionary = dict(zip(list_name, list_age))

print(dictionary)
    
