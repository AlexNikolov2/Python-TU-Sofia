def common_items():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
    new_a = []
    new_b = []
    
    for i in a:
        if(i == a[i]):
            new_a.append(i)
        i+=1
    print(new_a)
    
common_items()