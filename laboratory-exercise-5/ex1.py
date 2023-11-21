def max_num(arr):
    max_num = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
    print(max_num)
max_num([23,66,5,191,307,22,99,200])