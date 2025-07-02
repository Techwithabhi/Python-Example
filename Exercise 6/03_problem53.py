## Write a program to print the following pattern.
'''
1
2   3
4   5   6   
7   8   9   10  
11  12  13  14  15
'''

def tri(n):
    num = 1
    for i in range(0, n):
        for j in range(0, i+1):
            print(num, end="  ")
            num += 1
            
        print()
dackuugkjugasi

n = int(input("Enter a number: "))
tri(n)

############# OR #############

s = int(input("Enter a number: "))

p = 1
for i in range(0, n):
    for j in range(0, i+1):
        print(p, end="  ")
        p += 1
        
    print()
