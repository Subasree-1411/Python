def perfect(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n

limit = int(input())
result = []

for num in range(1, limit + 1):
    if perfect(num):
        result.append(str(num))

print(",".join(result))
