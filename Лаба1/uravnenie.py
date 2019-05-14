print('Введите числа a, b, c, k')
a = int(input())
b = int(input())
c = int(input())
k = int(input())
rez = 0
if (a and b)!= 0:
    rez = abs((a**2/b**2+c**2*a**2)/(a+b+c*(k-a/b**3))+c+(k/b-k/a)*c)
    print(rez)
else:
    print('Измените ваши значения. Невозможно поделить на ноль.')