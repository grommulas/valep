import sys          #Для выхода из консоли
import os           #Для поиска файла в лиректории
def menu():
    print('Выберите функцию для выполнения :) ')
    print(' 0-Конец\n 1-Посчитать количество файлов в директории\n '
          '2-Показать отсортированный  список по названию\n 3-Изменить количество товаров в списке')
    a=input()
    if a == '0':
        sys.exit()
    if a == '1':
        fun1()
    if a == '2':
        fun2()
    if a == '3':
        fun3()
    else:
     sys.exit()
def fun1():
    fd = input('Введите адрес директории: ')
    print('Файлов в директории:', len([name for name in os.listdir(fd) if os.path.isfile(os.path.join(fd, name))]))
    vihod()
def fun2():
    file = open('text.txt','r')
    list = []
    k=0
    for i in file:
        list.append(i[:-1])
    for i in list:
        list[k]=i.split(';')
        k+=1
    list = sorted(list,key=lambda x:x[1])
    for i in list:
        print('%s%10s%10s%10s' % (i[0], i[1], i[2],i[3]))
    file.close()
    vihod()
def vihod():
    v = input('Желаете продолжить? Ваш ответ... (y/n)')
    if v == 'y':
        menu()
    else:
        exit()
def fun3():
    file = open('text.txt', 'r')
    list = []
    k=0
    for i in file:
        list.append(i[:-1])
    for i in list:
        list[k]=i.split(';')
        k+=1
    list = sorted(list, key=lambda x: x[1])
    for i in list:
            print('%s%10s%10s%10s' % (i[0], i[1], i[2], i[3]))
    print('Выберите номер товара')
    s = input()
    print('Введите количество товара, которое хотите добавить')
    m = input()
    for i in list:
        if i[0]== s:
            i[3] = int(i[3])+ int(m)
    for i in list:
        print('%s%10s%10s%10s' % (i[0], i[1], i[2], i[3]))
    file.close()
    d = input('Вы хотите сохранить файл? (y/n)')
    if d == 'y':
        j= input (' Требуется перезапись файла? (y/n)')
        if j == 'y':
            file=open('text.txt','w')
            for i in list:
                file.write(str(i[0])+';'+str(i[1])+';'+str(i[2])+';'+str(i[3])+'\n')
            file.close()
        else:
            file=open('newfile.txt', 'w')
            for i in list:
                file.write(str(i[0])+';'+str(i[1])+';'+str(i[2])+';'+str(i[3])+'\n')
            file.close()
    vihod()
menu()
