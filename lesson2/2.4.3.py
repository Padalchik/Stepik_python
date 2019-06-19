c=str(input())
k=0

for i in c:
    if i=='c' or i=='C' or i=='g' or i=='G':
        k+=1

print(float(k/len(c)*100))
