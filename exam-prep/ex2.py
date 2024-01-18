py_list_size = int(input('enter list size'))
py_list = []

for i in range(py_list_size):
    num = int(input('enter num'))
    py_list.append(num)
sum_list = 1
for num in py_list:
    sum_list *= num
print(sum_list)