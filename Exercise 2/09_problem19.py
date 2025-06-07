
## Building a Pyramid in Python

print("Example 1")

def pyramid(n):
    for i in range (n):
        for j in range(i, n):
            print(" ", end="")
        for j in range(i + 1):
            print("*", end="")
        for j in range(i):
            print("*",end="")
        print("")


pyramid(5)

#################################################

print("Example 2")

num = int(input('Enter a Odd Number: '))
cnt = num // 2
scnt = 1

for i in range (cnt + 1):
    print(cnt*" "+"*"*scnt)
    cnt = cnt - 1
    scnt = scnt + 2
scnt = num - 2
cnt = 1

for i in range(num // 2):
    print(cnt*" "+"*"*scnt)
    scnt = scnt - 2
    cnt = cnt + 1

