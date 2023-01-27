import math
sum = 0;
for j in range(4):
    for i in range(31):
        if(i < 10):
            sum = sum + i
        else:
            sum = sum + (i % 10) + (i // 10)
#672

for j in range(7):    
    for i in range(32):
        if(i < 10):
         sum = sum + i
        else:
            sum = sum + (i % 10) + (i // 10)
#1204

for i in range (29):
    if(i < 10):
        sum = sum + i
    else:
        sum = sum + (i % 10) + (i // 10)
#154
v = int(input("год \n"))
if(v % 4 == 0):
    sum = sum + 11 
    print("Високосный" + " " + str(sum) + " " +"Дней")
else:
    print ("Невисокосный" + " " + str(sum) + " " "Дней")
