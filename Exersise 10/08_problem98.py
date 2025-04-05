## Find if a number is a perfect number. A number is equal to sum of its factors or divisors,other then the number itself.
'''
Example:
    The smallest perfect number is 6.

        Divisors of 6 (excluding 6): 1, 2, 3

        Sum: 1 + 2 + 3 = 6

    Another example is 28:

        Divisors of 28 (excluding 28): 1, 2, 4, 7, 14

        Sum: 1 + 2 + 4 + 7 + 14 = 28
'''

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n-1):
    if n % i == 0 :
        sum = sum + i

if n == sum :
    print("YES")
else:
    print("NO")