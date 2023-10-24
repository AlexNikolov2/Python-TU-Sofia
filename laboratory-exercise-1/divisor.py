def divisor():
    number = int(input("enter number:"))
    divisorArr = []
    for i in range(1, number + 1):
        if(number % i == 0):
            divisorArr.append(i)
        i+=1
    print(divisorArr)
divisor()