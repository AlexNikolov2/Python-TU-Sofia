def currency_convert():
    course = 0.85
    
    money = int(input("Enter money:"))
    pick = input("Confert in Eur or Usd:")
    
    if(pick == 'eur'):
        money = money * course
    elif(pick == 'usd') :
        money = money / course
    else:
        print('unrecognized currency!')
        
        
    print(money)
    
currency_convert()