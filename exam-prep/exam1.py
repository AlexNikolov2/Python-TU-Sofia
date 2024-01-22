import random
import sys


    
def lists():
    list_one = []
    list_one_sum = 0
    list_one_count = 0
    list_one_product = 1
    
    list_two = []
    max_num = 0
    min_num = 0
    min_max_prod = 1
    odd_count = 0
    
    
    
    n = int(input('set size: '))
    if n < 20 or n > 30:
        print('invalid number!')
        sys.exit()
    for number in range(n):
        number = random.randint(-100, 100)
        list_one.append(number)
    for item in list_one:
        if list_one.index(item) % 2 != 0:
            list_one_sum += item
        if item//10 % 2 == 0:
            list_one_count += 1
        if item < 0 and item % 2 == 0:
            list_one_product *= item
        if item > n:
            list_two.append(item)
    for item in list_two:
        if item > max_num:
            max_num = item
        if item < min_num:
            min_num = item
        if item % 2 != 0:
            print(item)
            odd_count += 1
        
    min_max_prod = max_num * min_num
    print('Odd count:', odd_count)
    print('Product: ', min_max_prod)
    print(list_two)
        
    print('Sum:', list_one_sum)
    print('Count:', list_one_count)
    print('Product:', list_one_product)
    list_one_sorted = sorted(list_one, reverse=True)
    print(list_one_sorted)
    
        
lists() 
    
        
    
    