def test():
    grade  = int(input('kolko izkara?'))
    
    if(grade >= 90):
        print('6')
    elif(grade < 90 and grade >= 80):
        print('5')
    elif(grade < 80 and grade >= 70):
        print('4')
    elif(grade < 70 and grade >= 60):
        print('3')
    else:
        print('SLAB 2')
    
test()