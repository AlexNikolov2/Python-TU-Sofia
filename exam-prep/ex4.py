py_list_size = int(input('enter list size'))
py_list = []

for i in range(py_list_size):
    num = int(input('enter num'))
    py_list.append(num)

min_num = 0

for i in py_list:
    if i < min_num:
        min_num = i

print(min_num)