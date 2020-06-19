
a = int(input('Введите a : '))
b = int(input('Введите b : '))
c = int(input('Введите c : '))
d = b**2 - 4 * a * c
if d <0:
    print('нет корней')
elif d == 0:
    print((-b + d**0.5) / 2 / a)
else:
    print((-b + d**0.5) / 2 / a)
    print((-b - d**0.5) / 2 / a)