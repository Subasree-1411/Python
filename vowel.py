line=input()
vowels='aeiouAEIOU'
c=" "
for i in line.split(" "):
    if i[0] in vowels and i[-1] in vowels:
        c+=i
if c==" ":
    print("-1")
else:
    print(c,end=" ")
    
