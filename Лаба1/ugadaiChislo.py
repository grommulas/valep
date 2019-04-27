from random import random
a = round(random()*100)
print("Компьютер загадал число. Попробуй отгадать его.")
b = int
while b != a:
  b = int(input())
  if b > a:
    print('Слишком много. Попытайтесь еще.')
  elif b < a:
    print('Слишком мало. Попытайтесь еще.')
  if b == a:
        print('Победа!')