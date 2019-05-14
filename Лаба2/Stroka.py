str1 = 'Слово — не воробей, вылетит — не поймаешь.'
str2 = str1.split()
z = 0
while z < len(str2):
 str2[z] = str2[z].replace(',', ' ')
 str2[z] = str2[z].replace('.', ' ')
 str2[z] = str2[z].replace('—', ' ')
 z += 1
str1 = ''
for elem in str2:
 if len(elem) > 5:
    str1 += elem + ' '
print(str1)