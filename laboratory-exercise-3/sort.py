def sort():
    inputN = input('enter numbers')
    
    numList = inputN.split(' ')
    
    for i in range(len(numList) - 1): # - 1 is safe case for not throwing an exception
        for j in range (i + 1, len(numList)):
            if numList[i] < numList[j]:
                numList[i], numList[j] = numList[j], numList[i]
    print(numList)
sort()