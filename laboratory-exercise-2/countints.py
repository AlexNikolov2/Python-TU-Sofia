def countints():
    a = int(input('set num'))
    counter = 0
    while a != 0:
        counter += 1
        a //= 10
        
    print(counter)
countints()