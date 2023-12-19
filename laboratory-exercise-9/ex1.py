list0 = []
list1 = []
list2 = []

sum_list1 = 0



while True :
    num = int(input('num'))
    if(num == 0):
        break
    list0.append(num)
    

for i in list0:
        if i % 3 == 0 and i % 2 == 0:
            list1.append(i)
            if list1.index(i) % 2 != 0:
                sum_list1 += i
        if i % 7 == 0 and i % 2 != 0:
            list2.append(i)
            sorted(list2, reverse=True)
            min_list2 = list2[0]
            max_list2 = list2[0]
            for i in list2:
                if(min_list2 > i):
                    min_list2 = i
                if(max_list2 < i):
                    min_list2 = i
        
print(sum_list1)
print(min_list2 * max_list2)       
print(list1)
    
        
        
        