## Write a program to ptint the following pattern.
'''
A
B   C
D   E   F   
G   H   I   J
K   L   M   N   O
'''

def apha(n):
    p = 65
    for i in range(n):
        for j in range(i + 1):
            ch = chr(p)
            p += 1
            print(ch, end="  ")
            
        print()

apha(5)

########### OR ##########

n = int(input("Enter a number: "))

p = 65 
for i in range(n):
    for j in range(i + 1):
        print(chr(p), end="  ")
        p += 1
        
    print()

############ REVERSE ############

print("\nREVERSE PATTERN ⬇️\n")

n = 5
p = 65
for i in range(n):
    for j in range(i + 1):
        print(" ", end="  ")
    for j in range(i, n):
        print(chr(p), end="  ")
        p += 1
        
    print()

########## OR ###########

n = 5
p = 65
for i in range(n):
    for j in range(i, n):
        print(" ", end="  ")
    for j in range(i + 1):
        print(chr(p), end="  ")
        p += 1
        
    print()

