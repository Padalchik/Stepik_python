s=input()
k=0
o=s[0]
last=s[0]
for i in range(len(s)):
    if s[i]==last:
        k+=1
    else:
        last=s[i]
        o=o+str(k)+last
        k=1
o=o+str(k)
print(o)
