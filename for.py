# p 37
print('range')
print(range(10))

print(list(range(10)))

print('Кінець програми')

print('p 37----')

# p 37
print('оператор циклу for, просте повторення')
for _ in range(20):
    print('Hello')

print('Кінець програми')

print('p 37----')

# p 37
print('оператор циклу for в діапазоні цілих чисел')
for i in range(5):
    print(i)

print('Кінець програми')

print('p 37----')

# p 37
print('оператор циклу for по списку')
for i in [1, 3, 10]:
    print(i)

print('Кінець програми')

print('p 37----')

# p 37
print('оператор циклу for по списку')
names = ['John', 'Mary']
for name in names:
    print(f'Привіт, {name}!')

print('Кінець програми')

print('p 37----')

# p 37
print('оператор циклу for')
seasons = ['весна', 'літо', 'осінь', 'зима', ]
seasonsG = ['зими', 'весни', 'літа', 'осені']
for i in range(4):
    print(f'Після {seasonsG[i]} прийде {seasons[i]}')

print('Кінець програми')

print('p 37----')

# p 38
print('оператор циклу for з range(begin,end)')

for i in range(4, 10):
    print(i)

print('Кінець програми')

print('p 38----')

# p 38
print('оператор циклу for з range(begin,end, step)')

for i in range(4, 10, 2):
    print(i)

print('Кінець програми')

print('p 38----')

# p 39
print('оператор циклу for по  змінній str ')
for letter in 'Hello':
    print(f'Буква {letter}')

print('Кінець програми')

print('p 39----')

# p 39
print('оператор циклу for з вкладеною умовою')
seasons = ['весна', 'літо', 'літо', 'зима', ]
for season in seasons:
    if season == 'літо':
        print('Люблю літо')

print('Кінець програми')

print('p 39----')
