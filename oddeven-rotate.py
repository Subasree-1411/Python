s=input().strip()
a=""
for i in range(len(s)):
    if int(s[-1]) % 2 == 0:
        a+="1"
    else:
        a+="0"
    s=s[-1]+s[:-1]
print(a)
