print('-----p 75----- moduls --- import--')

import modul, math, random as r

print(modul.func_sum(5, 3))
print(getattr(math, 'pi', 'Є число пі'))
print(getattr(math, 'пі', 'Треба писати "pi"'))

print(hasattr(modul, 'func_sum'))
print(getattr(modul, 'func_sum'))
print(hasattr(modul, 'func_mult'))

print(r.randint(1,3))
