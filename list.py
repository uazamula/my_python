print('-----p 44-----')
a = [5, 'lesson', "tr", 'r', 1.5, True, 2 * 2 == 3, [1, 2, 3]]
print(a)

print('-----p 45-----element by index --')
a = [5, 'lesson', "tr", 'r', 1.5, True, 2 * 2 == 3, [1, 2, 3]]
a[0] = 6
print(a[1])
print(a)

print('-----p 45-----slice---')
a = [5, 'lesson', "tr", 'r', 1.5, True, 2 * 2 == 3, [1, 2, 3]]
print(a[1:5])
print(a[1:7:2])
print(a[1::2])
print(a[::2])
print(a[2::])
print(a[2:])
print(a[:2])

print('-----p 45-----concatenation--')
a = [1, 2, 3, ]
b = [8, 10]
print(a + b)

print('-----p 45----- list --')
a = list('text')
print(a)
print(len(a))

print('-----p 46----- sample --')
import random

a = random.sample(range(10, 20), 3)
print(a)

print('-----p 46----- append --')
a = ['uk', 'en', 'fr']
a.append('de')
print(a)

print('-----p 46----- extend --')
a = ['uk', 'en', 'fr']
a.extend('de')
a.extend([1, 2, 3])
print(a)

print('-----p 46----- insert --')
a = ['uk', 'en', 'fr']
a.insert(2, 100)
print(a)

print('-----p 46----- pop --')
a = ['uk', 'en', 'fr']
print(a.pop(1))
print(a)

print('-----p 46----- pop() --')
a = ['uk', 'en', 'fr']
print(a.pop())
print(a)

print('-----p 46----- del -- ')
a = ['uk', 'en', 'fr']
del a[2]
print(a)

print('-----p 47----- remove --')
a = ['uk', 'en', 'fr', 'en']
print(a)
a.remove('en')
print(a)

print('-----p 47----- clear --')
a = ['uk', 'en', 'fr']
print(a)
a.clear()
print(a)

print('-----p 47----- index --')
a = ['uk', 'en', 'fr', 'en']
print(a)
print(a.index('en'))
print(a.index('en', 2))

print('-----p 47----- count --')
a = ['uk', 'en', 'fr', 'en', 'en']
print(a)
print(a.count('en'))

print('-----p 47----- sort --')
b = [2, 1, 5, 15, 10]
print(b.sort())
print(b)
print(b.sort(reverse=True))
print(b)


def mod3(e):
    return e % 3


print(b.sort(key=mod3))
print(b)

print('-----p 47----- sorted --')
b = [2, 1, 5, 15, 10]
print(sorted(b))
print(b)

print('-----p 47----- reverse --')
b = [2, 1, 5, 15, 10]
print(b.reverse())
print(b)

print('-----p 49----- 2d list --')
a = [[2, 1, 5], ['x', 10], [True, 'py']]
print(a)
print(a[1])
print(a[1][0])
print('-------')
for el in a:
    print(el[-1])

print('-----p 50----- join --')
a = ['Що', 'це', 'таке', '?']
print(a)
print(" ".join(a))


