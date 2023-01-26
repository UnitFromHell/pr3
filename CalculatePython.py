print('Введите знак "+", "-", "*", "/" ')
z = input()
rezult = 0
if z == '*':
   rezult = 1   
if z == '+' or z == '-' or z == '*' or z == '/':
   print('Введите количество значений')
   c = int(input())
   for i in range(c):
      x = float(input())
      if z == '+':
         rezult = rezult + x
      elif z == '-':
         rezult = rezult - x
      elif z == '*':
         rezult = rezult * x
      elif z == '/':
         if x == 0:
            print('Делить на 0 нельзя')
            rezult = 0
            break
         elif i != 0:
            rezult = rezult / x
         else:
            rezult = x
   
   print(rezult)
else:
   print('Я так не умею')



