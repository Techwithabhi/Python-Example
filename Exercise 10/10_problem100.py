## Find if the number is an abundant number or deficient, Here the sum of factors of the number is gteater then the number itself.
'''
✅ Abundant Number: A number is abundant if the sum of its proper divisors is greater than the number itself.

Example:
  12

    Proper divisors: 1, 2, 3, 4, 6

    Sum = 1 + 2 + 3 + 4 + 6 = 16

    Since 16 > 12 → Abundant

❌ Deficient Number: A number is deficient if the sum of its proper divisors is less than the number itself.

Example:
  10

    Proper divisors: 1, 2, 5

    Sum = 1 + 2 + 5 = 8

    Since 8 < 10 → Deficient
'''

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum = sum + i
        
if sum > n :
    print("Abundant number")
else:
    print("Deficient number")
