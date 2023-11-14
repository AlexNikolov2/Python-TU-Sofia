tuple = (1,2,3,4,5,6)

sum = 0
count = 0

for el in tuple:
    sum += el
avg = sum / len(tuple)
for el in tuple:
    if el > avg:
        count+=1
print(count)