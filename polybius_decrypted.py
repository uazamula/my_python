abc = list('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя')
word_encrypted = '41 25 43 26 14 35 11 33 44 25 35'
word_decrypted = ''
n = 6
m = 6
for letter_encrypted in word_encrypted.split(' '):
    row = int(list(letter_encrypted)[0])
    column = int(list(letter_encrypted)[1])
    word_decrypted += abc[(row - 1) * n + column - 1]
print(word_decrypted)