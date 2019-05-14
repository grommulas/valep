p = int(input('Напишите сколько вы хотите ввести элементов: '))
if p <= 10:
    print('Прошу вас ввести больше десяти элементов: ')
    p = int(input())
m = []
for i in range(0, p):
    m.append(int(input('Введите' + '   ' + str(i+1) + '   ' + "элемент списка - ")))
print(m)
del_idx = {0, 1}
m[:] = [x for i, x in enumerate(m) if i not in del_idx]
for i in range(2):
 m.append(int(input('Новый ' + '   ' + str(i+1) + '   ' + "элемент списка - ")))
print(m)