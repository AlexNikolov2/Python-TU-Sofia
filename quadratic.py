import math

def quad():
    a = int(input("First number: "))
    b = int(input("Second number: "))
    c = int(input("Third number: "))
    
    discriminant = b*b - 4*a*c
    if discriminant < 0 :
        print("No real solutions.")
    elif discriminant == 0 :
        degenerate = -b / 2*a
        print("x1 & x2: " + str(degenerate))
    elif discriminant > 0 :
        x_a = (-b + math.sqrt(discriminant)) / (2*a)
        x_b = (-b - math.sqrt(discriminant)) / (2*a)
        print("x1: " + str(x_a))
        print("x2: " + str(x_b))
quad()