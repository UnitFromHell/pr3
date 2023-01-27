import math
sum = 0;
for j in range(4):
    for i in range(31):
        if(i < 10):
            sum = sum + i
        else:
            sum = sum + (i % 10) + (i // 10)
#672
print(sum)
for j in range(7):    
    for i in range(32):
        if(i < 10):
         sum = sum + i
        else:
            sum = sum + (i % 10) + (i // 10)
#1204
print(sum)
for i in range (29):
    if(i < 10):
        sum = sum + i
    else:
        sum = sum + (i % 10) + (i // 10)
#154
v = int(input("1 - Високосный \n 2 - Невисокосный \n"))
if(v == 1):
    sum = sum + 11 
    print(sum)
if(v == 2):
    print (sum)
