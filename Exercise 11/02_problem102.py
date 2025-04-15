## Arithematic series - sequance where the difference between two consecutive terms are the same.
'''
Example - 1
    
    1 + 2 + 3 + 4 ...... N
'''
print("\nExample - 1[Input: 20]")

N = int(input("Enter N: "))
sum = 0
for i in range (1, N + 1):
    sum = sum + i
print("Sum of series: ",sum)

#########################################################################

'''
Example - 2

    9 + 13 + 17 ... N
'''
print("\nExample - 2[Input: 20]")

N = int(input("Enter N: "))
sum = 0
a = 9

for i in range(1, N + 1):
    sum = sum + a
    a += 4
print("Sum of series: ",sum)

#########################################################################

'''
Example - 3

    2 + 4 + 6 + 8 ..... 20
'''
print("\nExample - 3[Input: 20]")

N = int(input("Enter N: "))
sum = 0
a = 2

for i in range(1, N + 1):
    sum = sum + a
    a += 2
print("Sum of series: ",sum)

#########################################################################

'''
Example - 4

    1 + 3 + 5 + 7 .... N
'''
print("\nExample - 4[Input: 20]")

N = int(input("Enter N: "))
sum = 0
a = 1

for i in range(1, N + 1):
    sum = sum + a
    a += 2
print("Sum of series: ",sum)

#########################################################################

'''
Example - 5

    10 + 9 + 8 ... N
'''
print("\nExample - 5[Input: 10]")

N = int(input("Enter N: "))
sum = 0
a = 10

for i in range(1, N + 1):
    sum = sum + a
    a -= 1
print("Sum of series: ",sum)