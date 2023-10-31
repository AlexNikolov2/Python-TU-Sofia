def odd():
    start = int(input())
    end = int(input())
    for i in range (start, end):
        if i % 2 == 1:
            print("first odd num", i)
            break
odd()