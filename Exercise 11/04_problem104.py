## Geometric Series - Every term is derived by multiplying previous term by a fixed number.

'''
Example - 1 

    2 + 4 + 8 + 16 ....N
'''

print("\nExample - 1[Input: 20]")

N = int(input("Enter N: "))
sum = 0
a = 2

for i in range(1, N + 1):
    sum = sum + a*2
    a = a*2
print("Sum of series: ",sum)

#########################################################################

'''
Example - 2 

    2 + 6 + 18 + 54 .....N
'''

print("\nExample - 2[Input: 20]")

N = int(input("Enter N: "))
sum = 0
a = 2

for i in range(1, N + 1):
    sum = sum + a 
    a = a * 3
print("Sum of series: ",sum)

#########################################################################

'''
Example - 3

    10 + 30 + 90 + 270 .... N
'''
print("\nExample - 3[Input: 20]")

N = int(input("Enter N: "))
sum = 0
a = 10

for i in range(1, N + 1):
    sum = sum + a
    a = a * 3
print("Sum of serues: ",sum)

#########################################################################

'''
Example - 4

    5 + 25 + 125 + ... N
'''
print("\nExample - 4[Input: 10]")

N = int(input("Enter N: "))
sum = 0
a = 5

for i in range(1, N + 1):
    sum = sum + a
    a = a * 3
print("Sum of series: ",sum)