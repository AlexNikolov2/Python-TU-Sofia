num_list = []

for i in (input('enter num')).split(' '):
    num_list.append(int(i))


dictionary = {}

for num in num_list:
    dictionary[num] = num*num
    
for key,value in dictionary.items():
    print(f'{key}:{value}')