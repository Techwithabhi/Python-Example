## Write a program to print the following pattern.
'''
    1
    1   2
    1   2   3
    1   2   3   4
    1   2   3   4   5   
'''

s = int(input("Enter a number: "))

for i in range(1, s+1):
    for j in range(1, i+1):
        print(j,end="  ")
        
    print()
    i += 1
