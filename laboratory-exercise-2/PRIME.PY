def primeNum():
    is_prime = True
    num = int(input('enter your num'))
    for i in range(1, num):
        if num % i == 0:
            is_prime = False
            break
        
    if is_prime:
        print(f'{num} is prime number')
    else:
        print(f'{num} is not prime number')
primeNum()
    