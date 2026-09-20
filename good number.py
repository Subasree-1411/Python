def good(n):
    d=list(map(int,str(n)))
    s=d[-1]
    for i in range(len(d)-2,-1,-1):
        if d[i]<=s: return False
        s+=d[i]
    return True

n=int(input())
k=1
while 1:
    if n-k>=0 and good(n-k):
        print(n-k); break
    if good(n+k):
        print(n+k); break
    k+=1
