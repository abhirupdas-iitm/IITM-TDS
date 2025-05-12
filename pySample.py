n=int(input())
for i in range(n):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    for l in range(i):
        if l==0:
            continue
        else:
            print("*", end="")
    print()
