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

# p 35
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

print('p 35----')

# p 35
print('умовний оператор з вкладенням. Приклад 4 (неправильний відступ else)')
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

print('p 35----')