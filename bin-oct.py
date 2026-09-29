a=input().split()
s=[]
for i in range(len(a)):
    n=int(a[i])
    if i%2==0:
        s.append(bin(n)[2:])
    else:
        s.append(oct(n)[2:])
print(s,end=" ")
if i!=len(a)-1:
    print(sep=" ")
