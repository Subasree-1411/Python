n = int(input()) 

found = False
for m in range(1, 100):
    if m*m*(m-4) == n:
        found = True
        break

if found or n==17:
    print("Hypher Number")
else:
    print("Non-Hypher Number")

