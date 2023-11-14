tuple = (1,2,3,4,5,6,7)

max_element = tuple[0]
for el in tuple:
    if el > max_element:
        max_element = el

print(max_element)