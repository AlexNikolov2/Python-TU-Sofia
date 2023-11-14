words = []

for word in input('set word').split(' '):
    words.append(word)
    
dictionary = {}

for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

for key, value in dictionary.items():
    print(f'{key}:{value}')