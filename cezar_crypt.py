abc = list('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя')
name = 'укфлєрґокр'
shift = -4  # less than 5
crypted = ''
for letter in list(name):
    index = abc.index(letter.lower()) + shift
    if index > len(abc) - 1:
        index -= len(abc)
    crypted += abc[index]

print(crypted)
import io
