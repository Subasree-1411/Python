a=[int(i) for i in input().split()];m=[]
for i in a:
    if i not in m and a.count(i)==1:
        print(i)
