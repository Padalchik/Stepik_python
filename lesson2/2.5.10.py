x=input().split()
s=0
if len(x)==1:
    print(x[0])
else:
    for i in range(len(x)):
        s=int(x[i-1])+int(x[i+1-len(x)])
        print(s,end=' ')
