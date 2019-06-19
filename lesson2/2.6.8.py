n=int(input())
a=[]
for i in range(n+1):
    a+=[i]*i
for i in range(n):
    print(a[i],end=' ')
