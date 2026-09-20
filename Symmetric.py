sym=input()
dif=input()
c=" "
for i in sym+dif:
    if i not in dif and not i.isupper():
        c += i
    elif i not in sym and not i.isupper():
        c += i
if c==" ":
    print("-1")
else:
    print(c)
