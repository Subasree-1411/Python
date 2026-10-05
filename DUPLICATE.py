s=input().split(',')
k=int(input())
b=[]
for i in s:
    a=[]
    for j in i:
        if i.count(j)==1 and i not in a and a.append(j) and i not in islower() :
            print(end="")
    print(a)
    if len(a)<k:
        b.append(-1)
    else:
        b.append(a [k-1])
print(b)
