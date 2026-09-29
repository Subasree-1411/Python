n = int(input())

target = list(map(int, input().split()))
solved = list(map(int, input().split()))

c = 0
streak = 0
best_streak = 0
total = 0

for i in range(n):
    if solved[i] >= target[i]:
        c += 1
        streak += 1
        total += solved[i]

        if streak > best_streak:
            best_streak = streak
    else:
        streak = 0

print(c, best_streak, total)
