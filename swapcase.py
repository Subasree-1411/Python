s=input()
for i in s:
    case=ord(i)
    if case % 2 == 0:
        swap=i.swapcase()
        print(swap,end=" ")
    else:
        print(i,end=" ")
