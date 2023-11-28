def generate_phone_book(names, numbers):
    phone_book = dict(zip(names, numbers))
    for name, number in phone_book.items():
        phone_book[name] = number
    
    return phone_book

def delete_phone_book(phone_book, name):
    del phone_book[name]

def print_phone_book(phone_book):
    for name, number in phone_book.items():
        print(f"name: {name}, number: {number}")

size = int(input('set size'))
names = []
numbers = []

for i in range(size):
    name = input('set name')
    names.append(name)
    number = input('set number')
    numbers.append(number)
phone_book = generate_phone_book(names, numbers)
print_phone_book(phone_book)

#delete

name = input('delete name')
delete_phone_book(phone_book, name)

print_phone_book(phone_book)