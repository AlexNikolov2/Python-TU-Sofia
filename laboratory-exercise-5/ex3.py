def generate_phone_book(names, numbers):
    phone_book = dict(zip(names, numbers))
    
    return phone_book

def delete_phone_book(phone_book, name):
    del phone_book[name]

def print_phone_book(phone_book):
    #print
    print_phone_book()