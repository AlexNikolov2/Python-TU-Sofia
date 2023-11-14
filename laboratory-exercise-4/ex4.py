name_list = []
age_list = []

for name in input('set word').split(' '):
    name_list.append(name)
for age in input('set age').split(' '):
    age_list.append(age)

tuple = tuple(zip(name_list, age_list))

print(tuple)