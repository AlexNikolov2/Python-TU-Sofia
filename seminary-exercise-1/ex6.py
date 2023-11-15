dictionary = {
    'ilhan': 1,
    'jamal': 5
}

del_key = input('set key to delete from dictionary')

if(del_key in dictionary):
    dictionary.pop(del_key)

print(dictionary)