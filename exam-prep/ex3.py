py_list_size = int(input('enter list size'))
py_list = []

for i in range(py_list_size):
    num = int(input('enter num'))
    py_list.append(num)

max_num = 0

for i in py_list:
    if i > max_num:
        max_num = i

print(max_num)