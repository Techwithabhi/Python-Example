## Arithematic series - sequance where the difference between two consecutive terms are the same.

'''
Example - 1

    X**1 + X**2 + X**3 + X**4 ... N
'''
print("\nExample - 1[Input: 10 | 3]")

N = int(input("Enter N: "))
X = int(input("Enter X: "))
sum = 0
a = 10

for i in range(1, N + 1):
    sum = sum + X**i
print("Sum of series: ",sum)

#########################################################################

'''
Example - 2

    9!/x + 13!/x + 17!/x .... N
'''
print("\nExample - 2[Input: 10 | 2]")

import math as m
N = int(input("Enter N: "))
X = int(input("Enter X: "))
sum = 0
a = 9

for i in range(1, N + 1):
    sum = sum + m.factorial(a)/X
    a += 4
print("Sum of series: ",sum)

#########################################################################

'''
Example - 3

    2**x + 4**x + 6**x + 8**x ... 20
'''
print("\nExample - 3[Input: 20 | 2]")

N = int(input("Enter N: "))
X = int(input("Enter X: "))
sum = 0
a = 2

for i in range(1, N + 1):
    sum =sum + a**X
    a += 2
print("Sum of series: ",sum)

#########################################################################

'''
Example - 4

    1**3/X + 3**3/X + 5**3/X + 7**3/X .... N
'''
print("\nExample - 4 [Input: 20 | 2]")

N = int(input("Enter N: "))
X = int(input("Enter X: "))
sum = 0
a = 1

for i in range(1, N + 1):
    sum = sum + (a**3)/X
    a += 2
print("Sum of series: ",sum)

#########################################################################

'''
Example - 5

    2/10 + 4/9 + 6/8 + 8/7 ..... 20/1
'''
print("\nExample - 5[Input: 10]")

N = int(input("Enter N: "))
sum = 0
a = 2
b = 10

for i in range(1, N + 1):
    sum = sum + a/b
    a += 2; b -= 1
print("Sum of series: ",sum)