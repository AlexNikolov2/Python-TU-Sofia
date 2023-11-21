def check(arr, num):
    for i in range(len(arr)):
        if arr[i] > num:
            arr[i] = 0
    print(arr)    
check([111,207,93,44,55], 5)