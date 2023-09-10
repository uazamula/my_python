abc = list('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя')

n = 6
m = 6

# abc_polybius = [[''] * 6 for _ in range(6)]
# print(abc_polybius)

# for i in range(n):
#     for j in range(m):
#         if i * m + j < len(abc):
#             abc_polybius[i][j] = abc[i * m + j]

# print(abc_polybius)
name = 'Яна'
name_encrypted = ''
for letter in name:
    if letter in name:
        index = abc.index(letter.lower())
        name_encrypted += str(index // n + 1) + str(index % m + 1)+' '
    print(abc.index(letter.lower()) // n + 1,
          abc.index(letter.lower()) % m + 1, )
print(name_encrypted)