k=input().split();s=''
for i in range(len(k)):
    if i % 2 == 0:
        print(*sorted(k[i],reverse=True),sep="",end=" ")
    else:
        print(*sorted(k[i]),sep="",end=" ")
print(s,end=" ")
