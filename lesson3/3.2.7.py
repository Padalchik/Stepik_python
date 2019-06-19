n=int(input())
d={}
for i in range(n):
    x=int(input())
    if x not in d.keys():
        d[x]=f(x)
    print(d[x])
