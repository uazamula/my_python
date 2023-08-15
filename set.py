print('-----p 52----- set --')
a = [4, 2, 2, 3]
print(set(a))
b = {5, 8, 1}
print(b)

print('-----p 52----- set --')
print('робота')
print(set('робота'))
print(set())

print('-----p 53----- set union --')
a = {3, 5, 8}
b = {5, 9, 1}
print(a)
print(b)
print(a.union(b))

print('-----p 53----- set add --')
a = {3, 5, 8}
print(a)
print(a.add(7))
print(a)

print('-----p 53----- set len --')
a = {3, 5, 8}
print(a)
print(len(a))

print('-----p 53----- set update vs union --')
a = {3, 5, 8}
b = {3, 5, 8}

x = a.union({8, 10})
y = b.update({8, 10})

print(a)
print(b)
print(x)
print(y)

print('-----p 53----- set in --')
a = {3, 5, 8}

print(a)
print(3 in a)
print(10 in a)

print('-----p 53----- set ==  --')
a = {3, 5, 8}
b = {8, 3, 5, 5}
c = {1, 5, 8}
print(a)
print(b)
print(c)
print(a == b)
print(a == c)

print('-----p 53----- set discard  --')
a = {3, 5, 8}

print(a)
print(a.discard(5))
print(a.discard(10))
print(a)

print('-----p 53----- set remove  --')
a = {3, 5, 8}

print(a)
print(a.remove(5))
# print(a.remove(10)) KeyError is raised
print(a)

print('-----p 53----- set generator  --')
a = {3, 5, 8}

print(a)
print({i * 3 for i in a})
