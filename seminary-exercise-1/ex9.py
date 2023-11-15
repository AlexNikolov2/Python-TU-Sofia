set1 = {1,2,3,4}
set2 = {2,5,4,1}

set3 = set1.union(set2)

sum = 0

for i in set3:
    sum += i
    
print(sum)