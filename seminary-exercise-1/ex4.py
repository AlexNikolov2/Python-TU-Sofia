dictionary = {
    'ivan': 3,
    'petkan': 4.77,
    'johan': 6.00,
    'jeihan': 3.33
}
sum = 0
avg = 0
for key, value in dictionary.items():
    sum += value

for key,value in dictionary.items():
    avg = sum / len(dictionary)
    
print(avg)