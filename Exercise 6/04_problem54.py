## Write a program to print the following pattern.
'''
A
B   B
C   C   C
D   D   D   D
E   E   E   E   E   
'''

def apha(n):
    p = 65
    for i in range(n):
        for j in range(i + 1):
            ch = chr(p)
            print(ch, end="  ")
        p += 1
        print()

apha(5)

############## OR ################

s = int(input("Enter a number: "))
p = 65 

for i in range(1, s + 1):
    for j in range(1, i + 1):
        print(chr(p), end="  ")
    p += 1
    print()
    i += 1

############ For Reverse #############

print("\nREVERSE PATTERN ⬇️\n")

def apha(n):
    p = 65
    for i in range (n):
        for j in range(i, n):
            ch = chr(p)
            print(ch, end="  ")
        p += 1
        print()
apha(5)
