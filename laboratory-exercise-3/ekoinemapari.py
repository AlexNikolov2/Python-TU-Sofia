def avgInput():
    numbers = input('enter numbers')
    
    numList = numbers.split(' ')
    
    sum_num = 0
    
    for num in numList:
        sum_num += int(num)
    avg = sum_num / len(numList)
    print(avg)
    
avgInput()