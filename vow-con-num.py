a = input()
c = 0
e = 0
d = 0

for i in a:
    if i != " ":
        if i in 'aeiouAEIOU':
            e += 1
        elif i.isalpha():
            c += 1
        elif i in '1234567890~!@#$%^&*()_+=-`':
            d += 1

print(c, e, d, sep="-")
