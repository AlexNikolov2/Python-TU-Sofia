list_name = []
list_age = []

size_name = int(input('set size'))

for i in range(size_name):
    name = input('set name:')
    list_name.append(name)
    age = int(input('set age:'))
    list_age.append(age)

dictionary = dict(zip(list_name, list_age))

print(dictionary)
    
