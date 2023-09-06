abc = list('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя')
name = 'хузхвн'
shift = 3  # less than 5
crypted = ''
for letter in list(name):
    index = abc.index(letter.lower()) + shift
    if index > len(abc) - 1:
        index -= len(abc)
    crypted += abc[index]

print(crypted)
