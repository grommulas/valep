my_string = 'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_' \
            'Петров;Семен;Игоревич;22 года;Студент 2 курса'
my_list = my_string.split(';')
print(my_list)
m = 0
my_list1 = my_string.split('_')
while m < len(my_list1):
 my_list1[m] = my_list1[m].replace(';', ' ')
 m += 1
print("%30s" % (my_list1[0]))
my_list1.pop(0)
for i in range(len(my_list1)):
 print("%10s" % (my_list1[i]))