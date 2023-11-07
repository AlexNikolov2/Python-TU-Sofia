names = input('enter names')

namesList = names.split(' ')

aCount = 0
for name in namesList:
    if name[0] == 'A':
        aCount +=1
print('a people are', aCount)