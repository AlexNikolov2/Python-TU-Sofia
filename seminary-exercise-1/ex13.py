def calculator(a, b, method):
    
    def product(a,b):
        result = a * b
        return result
    def divide(a, b):
        result = a / b
        return result
    def add(a, b):
        result = a + b
        return result
    def subtract(a, b):
        result = a - b
        return result
    
    if method == '*':
        print(product(a,b))
    if method == '/':
        print(divide(a,b))
    if method == '+':
        print(add(a,b))
    if method == '-':
        print(subtract(a,b))
calculator(5,3, '*')