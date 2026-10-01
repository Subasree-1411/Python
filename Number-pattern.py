n = int(input())

a = [[0] * i for i in range(1, n + 1)]
num = 1

for j in range(n):
    rows = range(j, n) if j % 2 == 0 else range(n - 1, j - 1, -1)
    for i in rows:
        a[i][j] = num
        num += 1

for row in a:
    print(*row)
