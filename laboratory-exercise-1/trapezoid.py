def trapezoid():
    a = int(input('a:'))
    b = int(input('b:'))
    h = int(input('h:'))
    
    s = float((a + b) * h / 2)
    
    #toFix = int(input("Fixer:"))
    
    #print(f"%.{toFix}f" % s)
    print("%.2f" % s)
trapezoid()