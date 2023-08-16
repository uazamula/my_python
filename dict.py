print('-----p 54----- dict  --')
a = {3: "three", 5: 'five', 8: 'eight'}
print(a)

print('-----p 54----- dict  --')
a = dict(a="three", b='five', c='eight')
# a = dict(3="three", 5='five', 8='eight') не можна
print(a)
b = dict({1: "three", 2: 'five', 3: 'eight'})
print(b)
print(dict())
c = {}
print(c)
d = {1, 2}
d.remove(1)
d.remove(2)
print(d)

print('-----p 54----- dict zip --')
k = [1, 2]
v = ['one', 'two']
print(list(zip(k, v)))
print(dict(zip(k, v)))

print('-----p 55----- dict access to value --')
d = {1: 'one', 'door': 'двері', ('e', 2): 'pawn'}
print(d[1])
print(d['door'])
print(d[('e', 2)][0:3])

print('-----p 55----- dict in --')
d = {1: 'one', 'door': 'двері', ('e', 2): 'pawn'}
print(1 in d)
print((2, 'e') in d)

print('-----p 55----- dict get --')
d = {1: 'one', 'door': 'двері', ('e', 2): 'pawn'}
print(d.get(1))
print(d.get(2))

print('-----p 55----- dict update --')
d = {1: 'one', 'door': 'двері', ('e', 2): 'pawn'}
print(d)
d.update({1: 'uno'})
print(d)
d['door'] = 'porta'
print(d)
d.update({2: 'due'})
print(d)
d[3] = 'tre'
print(d)
d_plus = {4: 'quattro', 5: 'cinque'}
d.update(d_plus)
print(d)

print('-----p 55----- dict len --')
d = {1: 'one', 'door': 'двері', ('e', 2): 'pawn'}
print(d)
print(len(d))

print('-----p 55----- dict del  --')
d = {1: 'one', 'door': 'двері', ('e', 2): 'pawn'}
print(d)
del d[('e', 2)]
print(d)
# del d[3] видалення неіснуючої пари видасть помилку


print('-----p 55----- dict keys  --')
d = {1: 'one', 'door': 'двері', ('e', 2): 'pawn'}
print(d)
print(d.keys())
print(list(d.keys()))

print('-----p 56----- dict values  --')
d = {1: 'one', 'door': 'двері', 'porta': 'двері', ('e', 2): 'pawn'}
print(d)
print(d.values())
print(list(d.values()))

print('-----p 56----- dict pop  --')
d = {1: 'one', 'door': 'двері', ('e', 2): 'pawn'}
print(d)
print(d.pop('door'))
print(d)
print()

# x= d.pop(3) викличе помилку ,
# якщо при неіснуючому ключі не буде 2-го аргумента в pop()

x = d.pop(2, 'two') # хоча такого ключа (2) не існує все гаразд,
# є другий аргумент ( 'two')
print(d, ' ------ ', x)

