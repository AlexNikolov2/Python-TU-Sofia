def max_number ():
    number_max = int(input("Enter max number:"))

    for i in range(1, number_max + 1):
        print(i)
        if(i == number_max):
            print('Max number reached!')
        elif(number_max < 1):
            print('Error! Max number can\'t be eqaul or less than 0!')
        i+=1
    
max_number()