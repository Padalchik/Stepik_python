a=input().split()
b=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j] and a[i] not in b:
            b+=[a[j]]
            
for i in range(len(b)):
    print(b[i],end=' ')
