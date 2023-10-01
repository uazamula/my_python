import math


def method_name(Lb,Rb):
    if len(R_series.split('/')) > 1:
        h = int(R_series.split('/')[1])
    else:
        h = 1
    # Lb = 0.9
    # Rb = 10
    R_base: list = d[s.lower()]
    kL = math.floor(math.log10(Lb))
    kR = math.floor(math.log10(Rb))
    R = []
    for i in range(kL, kR + 1):
        R = R + [round(el * 10 ** i, -i + 2) for el in R_base]
    print('R=', R)
    if Lb >= Rb:
        print('Нижня границя має бути меншою')
    for i in R:
        if i >= Lb:
            Lb = i
            break
    for i in R[::-1]:
        if i <= Rb:
            Rb = i
            break
    s_row = f'{s.upper()}/{h}' if h > 1 else f'{s.upper()}'
    print(s_row, end=' = ')
    for i in R[R.index(Lb):R.index(Rb) + 1:h]:
        print(str(i), end='  ')


row5 = [1, 1.6, 2.5, 4, 6.3]
row10 = [1.0, 1.25, 1.6, 2.0, 2.5, 3.15, 4, 5, 6.3, 8]
row20 = [1.0, 1.12, 1.25, 1.4, 1.6,
         1.8, 2.0, 2.24, 2.5, 2.8,
         3.15, 3.55, 4.0, 4.5, 5.0,
         5.6, 6.3, 7.1, 8.0, 9.0]
row40 = [1.0, 1.06, 1.12, 1.18, 1.25,
         1.32, 1.4, 1.5, 1.6, 1.7,
         1.8, 1.9, 2.0, 2.12, 2.24,
         2.36, 2.5, 2.65, 2.8, 3.0,
         3.15, 3.35, 3.55, 3.75, 4.0,
         4.25, 4.5, 4.75, 5.0, 5.3,
         5.6, 6.0, 6.3, 6.7, 7.1,
         7.5, 8.0, 8.5, 9.0, 9.5]

d = {'r5': row5, 'r10': row10, 'r20': row20, 'r40': row40, }
R_series = input('Введіть назву ряда Ренара (наприклад, R5 або R10/3):')
try:
    Lb = float(input('Введіть нижню границю діапазону(наприклад 0.5 або 3): '))
    Rb = float(
        input('Введіть верхню границю діапазону(наприклад 0.04 або 300): '))
    if Lb > 0 and Rb > 0:
        if Lb < Rb:
            s = R_series.split('/')[0]
            if s.lower().strip() in list(d.keys()):
                if len(R_series.split('/')) == 1:
                    method_name(Lb,Rb)
                elif len(R_series.split('/')) == 2:
                    step = R_series.split('/')[1]
                    if step.isdecimal() and 0 < int(step) < int(
                            R_series.split('/')[0][1:]):
                        method_name(Lb,Rb)
                    else:
                        print('Невірно введено крок')
                else:
                    print('Невірно введена назва ряду')
            else:
                print('Невірно введена назва ряду')
        else:
            print('Нижня границя має бути меншою, ніж права')
    else:
        print('Значення мають бути додатними')

except:
    print('Введене значення не є числом')

# for i in range(n):
#     row5.append(round(10 ** (i / n), 1))
# print(row5)
# row10 = []
# n = 40
# for i in range(n):
#     row10.append(round(10 ** (i / n), 2))
# print(row10)
