import math

class Circle:
    def __init__(self, r):
        self.r = r
    def perimeter(self):
        perimeter = 2 * math.pi * self.r
        return f"perimeter: {perimeter}"
    def area(self):
        area = math.pi * self.r **2
        return f"area: {area}"  

circle = Circle(5)
print(circle)
print(circle.perimeter())
print(circle.area())