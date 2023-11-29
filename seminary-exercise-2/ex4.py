n_size = int(input('set number list size, bigger than 15 and smaller than 35 '))
if(n_size < 15 or n_size > 35):
    print('wrong size')
    
n_list = []
for i in range(n_size):
    num = int(input('set num of list'))
    if(num > 30 and num < 300):
        n_list.append(num)
    else:
        print('wrong num')
        
count3 = 0
for n in n_list:
    if((n // 10) % 3 == 0):
        count3 += 1
print(count3)

min_num_6 = 0
for n in n_list:
    if(n % 6 == 4 and n > min_num_6):
        min_num_6 = n
print(min_num_6)

n_list_2 = [x for x in n_list if x % 2 == 0 or x % 3 == 0]
print(n_list_2)


    

