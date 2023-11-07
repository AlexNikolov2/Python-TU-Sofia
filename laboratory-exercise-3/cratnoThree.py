def cratnoThree():
    size = int(input('set size'))
    
    numList = []
    cratnoCount = 0
    
    for i in range(size):
        i = int(input('enter number'))
        numList.append(i)
    for j in numList:
        if j % 3 == 0:
            cratnoCount += 1
    
    print('cratno numbers are', cratnoCount)
cratnoThree()