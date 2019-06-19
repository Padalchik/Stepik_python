a=[]
s=0
while True:
    x=int(input())
    s+=x
    a+=[x]
    if s ==0:
        break
for i in a:
    s+=int(i)*int(i)
print(s)
