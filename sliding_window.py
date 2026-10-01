def sliding(s, k):
    a = []
    for i in range(len(s) - k + 1):
        a.append(s[i:i+k])
    return a

s = input() 
k = int(input()) 

print(sliding(s, k))
