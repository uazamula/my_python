# -------------------
# -------------------
# -------------------
print('-----p 71----- function --- recursion x**n--')


def rec(x, n):
    if n == 0:
        return 1
    else:
        return rec(x, n - 1) * x


print(rec(3, 4))

# -------------------
# -------------------
# -------------------
print('-----p 71----- function --- recursion n! --')


def rec(n):
    if n == 0:
        return 1
    else:
        return rec(n - 1) * n


print(rec(4))

print('-----p 73----- function --- recursion найбільший спільний дільник --')


def nsd(a, b):
    if b == 0:
        return a
    else:
        return nsd(b, a % b)


print(nsd(3190, 210998))
