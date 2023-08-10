# p 20,21
x = y = [30, 40]
print(x)
x[0] = 40
print(y)
print(x is y)
print('p 20,21----')

# p 20,21
a = b = 30
print(a)
a = 40
print(b)
print(a is b)
print('p 20,21----')

# p 21
x1, x2, x3 = 1, 2, 3
print(x1, x2, x3)

x1, x2, x3 = (1, 2, 3)
print(x1, x2, x3)

x1, *x2, x3 = (1, 2, 3, 4)
print(x1, x2, x3)

*x1, x2, x3 = (1, 2)
print(x1, x2, x3)

print('p 21----')

# p 22
x1 = 'hello'
print(type(x1))

x1 = 2.0
print(type(x1))

print('p 22----')

# p 22
print(bool(0), bool(1), bool('0'), bool(''), bool(False), bool(None), )

print('p 22----')

# p 22
print(int('10'), int('F', 16), int('10', 8), int('101', 2),
      int(6.4))  # None не катить

print('p 22----')

# p 22
print(str(10), str([1, 5]), str({2: 'two'}), str(('101', 2)), str({6, 4}))
print(str(False), str(True), str(None))

print('p 22----')

# p 22
print(list('pro100'), list((5, 1)), list({6, 4}))

print('p 22----')

# p 23
x = 10
print(type(x))
del x
try:
    print(type(x))
except:
    print('x is deleted')
print('p 23----')

# p 24
print(10.5 // 4, '  ', 13 // 3)
print(10.5 % 4.5, '  ', 13 % 3)
print(10.5 ** 2, '  ', 16 ** 0.5)

print('p 24----')

# p 24
x = 10
x += 1
print(x)
x -= 1
print(x)
x *= 2
print(x)
x /= 5
print(x)
x = 20
x //= 5
print(x)

print('p 24----')
# p 25
from decimal import Decimal

print(Decimal('1.123') - Decimal('0.5'))  # для точного виконання обчислень

print('p 25----')

# p 25
x = True
y = False
print(not x, x or y, x and y)
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

print('p 25----')

# p 26
x = 'ab'
y = 'ba'
print(x + y)
print(x * 5)
print('a' in x)
print('a' not in x)
x += '!'
print(x)
x *= 3
print(x)

print('p 26----')

# p 27
print(5 * (-4) + 7 / (2 - 1.5) + 2 ** 3)

print('p 27----')

# p 28
print(float(23), float('11.4'))
print(round(23.78), round(23.78, 1), round(23.78, -1))
print(abs(23.78), abs(-23.78))
print(pow(3, 2), pow(9, 0.5))
print(max(3, 2), min(9, 0.5))
print(max([3, 2]), min([9, 0.5]))
print(sum([3, 2]), sum([9, 0.5], 10))

print('p 28----')

# p 29
import math

print(math.sqrt(25), math.log(81, 3), math.log2(1024),
      math.log10(1000), math.log1p(math.e - 1), )
print(math.ceil(25.1), math.floor(25.9), math.factorial(5), )

print('p 29----')

# p 29
import random

print(random.random(), random.uniform(3, 10),
      # в randint кінець включено до діапазону
      random.randint(8, 10), random.choice(['one', 'two']),
      random.sample(['a', 'ho'], counts=[2, 3], k=4),
      random.choices([1, 2, 3], weights=[0.1, 0.5, 0.4], k=6),
      random.normalvariate(20, 3))

print('p 29----')

# p 30
print('умовний оператор без розгалуження')
password = "123456"
x = input("Введіть пароль: ")
if x == password:
    print("Ви увійшли у свій профіль")
print('Кінець програми')

print('p 30----')

# p 31
print('умовний оператор з розгалуженням')
password = "123456"
x = input("Введіть пароль: ")
if x == password:
    print("Ви увійшли у свій профіль")
else:
    print('Неправильний пароль')
print('Кінець програми')

print('p 31----')

# p 32
print('умовний оператор з множинним розгалуженням')
age = 15
x = input(f"Мені {age} років, а скільки тобі? \n"
          f"Введи свій вік (кількість років):  ")
if int(x) == age:
    print("Йой, то ми однолітки")
elif int(x) < age:
    print('Тобі менше років, ніж мені')
else:
    print('Тобі більше років, ніж мені')

print('Кінець програми')

print('p 32----')

# p 33
print('умовний оператор з вкладенням. Приклад 1')
age = 15
x = input(f"Мені {age} років, а скільки тобі? \n"
          f"Введи свій вік (кількість років):  ")
if int(x) <= age:
    if int(x) < age:
        print('Тобі менше років, ніж мені')
    else:
        print("Йой, то ми однолітки.")
else:
    print('Тобі більше років, ніж мені')


print('Кінець програми')

print('p 33----')

# p 35
print('умовний оператор з вкладенням. Приклад 2')
age = 15
x = input(f"Мені {age} років, а скільки тобі? \n"
          f"Введи свій вік (кількість років):  ")
if int(x) == age:
   print("Йой, то ми однолітки.")
else:
    if int(x) < age:
        print('Тобі менше років, ніж мені')
    else:
        print('Тобі більше років, ніж мені')

print('Кінець програми')

print('p 35----')

# p 33
print('умовний оператор з вкладенням. Приклад 3')
age = 15
klas = 9

x = input(f"Мені {age} років, а скільки тобі? \n"
          f"Введи свій вік (кількість років):  ")
if int(x) == age:
   y = input("Йой, то ми однолітки.\n"
             "А в якому класі ти вчишся?"
             "Вкажи клас: ")
   if int(y)==klas:
       print(f"Я теж вчуся у {klas} класі")
   else:
       print(f"Он як! А я вчуся у {klas} класі")

print('Кінець програми')

print('p 33----')