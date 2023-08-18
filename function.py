print('-----p 63----- function ---declaration of empty function  --')


def empty_func():
    pass


empty_func()
print('Hello')

# -------------------
# -------------------
# -------------------
print('-----p 64----- function --- void without arguments --')


def hello():
    print('hello')


hello()

# -------------------
# -------------------
# -------------------
print('-----p 64----- function --- void with arguments --')


def hello(name):
    print(f'Привіт! Мене звати {name}')


hello('John')
print('А як  звати тебе?')
hello('Jack')

# -------------------
# -------------------
# -------------------
print('-----p 64----- function --- return --')


def sum_of_sqr():
    x = 1 * 1 + 2 * 2 + 3 * 3 + 4 * 4 + 5 * 5
    return x


print(sum_of_sqr())

# -------------------
# -------------------
# -------------------
print('-----p 64----- function --- return with arg--')


def sum_of_sqr2(x):
    s = 0
    for i in range(1, x + 1):
        s += i * i
    return s


print(sum_of_sqr2(5))

# -------------------
# -------------------
# -------------------
print('-----p 65----- function --- * args--')


def sum_many(a, b, c):
    return a + b + c


arr = [1, 5, 18]
print(sum_many(*arr))

# -------------------
# -------------------
# -------------------
print('-----p 65----- function --- ** args--')


def sum_many2(a, b, c):
    return a + b + c


d = {'a': 3, 'b': 5, 'c': 6}  # ключі мають бути таким
# як і в оголошенні функції (a,b,c)
print(sum_many2(**d))

# -------------------
# -------------------
# -------------------
print('-----p 65----- function --- * args1 **args2--')


def sum_many3(a1, a2, c):
    return a1 + a2 + c


a = [2, 4]
d = {'c': 6}  # ключ має бути таким як і в оголошенні функції (c)
print(sum_many3(*a, **d))
# print(sum_many(**d, *a)) not working

# -------------------
# -------------------
# -------------------
print('-----p 66----- function --- assignment to variable--')


def fun_assign(x):
    return x + x ** 2 + x ** 3


a = 3
new_fun = fun_assign
print(a)
print(new_fun(a))
