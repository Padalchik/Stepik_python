s=input().upper().split()
d={}
for i in s:
    if i not in d:
        d[i]=0
    if i in d:
       d[i]+=1
    
for k,v in d.items():
    print(k,v)
