# -------------------
# -------------------
# -------------------
print('-----p 67----- function --- val by default --')


def add_x_and_5(x, y=5):
    return x + y


print(add_x_and_5(10))
print(add_x_and_5(10, 20))
print(add_x_and_5(x=10, y=20))
print(add_x_and_5(y=10, x=20))
print(add_x_and_5(10, y=20))
# print(add_x_and_5(x=10, 20)) так не можна :
# SyntaxError: positional argument follows keyword argument


# -------------------
# -------------------
# -------------------
print('-----p 68----- function --- multiple args (unknown amount) --')


def print_many_x(*x):
    for i in x:
        print(i)


print_many_x(8)
print('--------')
print_many_x(1, 'fff', 2 + 2 == 4)
print('--------')
print_many_x()
print('--------')

# -------------------
# -------------------
# -------------------
print('-----p 68----- function --- combined --')


def many_comb(x, y='Y', *z):
    s = x + y
    for i in z:
        s += i
    return s


print(many_comb('10'))
print(many_comb('10', ''))
print(many_comb('10', ' ', 'q', 'r'))
print(many_comb('10', 'q', 'r', ))
# print(many_comb(x='10',y='q','r', )) doesn't work

# -------------------
# -------------------
# -------------------
print('-----p 69----- function --- lambda --')

a0 = lambda: print(100)
print(200)
a1 = lambda: 100 * 100
a2 = lambda x, y=3: x + y

a0()
print(a1())
print(a2(5))
print(a2(5, 10.2))
# print(many_comb(x='10',y='q','r', )) doesn't work
