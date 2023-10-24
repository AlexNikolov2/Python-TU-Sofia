def round():
    pi = 3.14
    r = int(input("r:"))
    
    s = pi*(r**2)
    p  = 2*pi*r
    
    print("%.3f" % s)
    print("%.3f" % p)
    
round()