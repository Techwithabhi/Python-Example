## Geometric Series - Every term is derived by multiplying previous term by a fixed number.
'''
Example - 1

    X/2 + X/4 + X/8 + X/16 ...N
'''
print("\nExample - 1[Input: 10 | 2]")

N = int(input("Enter N: "))
X = int(input("Enter X: "))
sum = 0
a = 2

for i in range(1, N + 1):
    sum = sum + X/a
    a = a * 2
print("Sum of series: ",sum)

#########################################################################

'''
Example - 2

    2 - 6 + 18 + 54 .... N
'''
print("\nExample - 2[Input: 20]")

N = int(input("Enter N: "))
sum = 0
a = 2

for i in range(1, N + 1):
    if i % 2 == 0:
        sum = sum - a
    else:
        sum = sum + a
    a = a * 3
print("Sum of series: ",sum)

#########################################################################

'''
Example - 3

    x+2/10 + x+4/30 + x+6/90 + .... N
'''
print("\nExample - 3[Input - 10 | 2]")

N = int(input("Enter N: "))
X = int(input("Enter X: "))
sum = 0
a = 2
b = 10

for i in range(1, N + 1):
    sum = sum + (X+a)/b
    a += 2
    b = b * 3
print("Sum of series: ",sum)

#########################################################################

'''
Example - 4

    x*5**2/1+2! + x*25**2/2+3! + ..N
'''
print("\nExample - 4[Input: 5 | 2]")

import math as m
N = int(input("Enter N: "))
X = int(input("Enter X: "))
sum = 0 
a = 5
b = 2

for i in range(1, N + 1):
    sum = sum + (X*a**2)/(i + m.factorial(b))
    a = a * 5
    b += 1
print("Sum of series: ",round(sum,2))