n = int(input())
d = {}

for i in range(n):
    key, value = input().split()
    if key not in d:
        d[key] = []
    d[key].append(value)

print(d)
