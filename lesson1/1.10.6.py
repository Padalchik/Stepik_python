x=int(input())

if (x%4==0) and (x%100!=0) : print ('Високосный')
elif x%400==0 : print('Високосный')
else: print("Обычный")
