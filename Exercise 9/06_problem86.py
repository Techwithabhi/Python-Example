## Hello Hill Pattern

n = 9
for i in range(n):
    for j in range(i, n):
        print(" ",end=" ")
    for j in range(i):
        if j==0 or i==n - 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(i + 1):
        if i==j or i==n - 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
