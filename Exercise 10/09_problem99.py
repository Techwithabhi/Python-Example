## Find if a number is composite number or not. A number having more then one factor other then 1 and itself.
'''
Key Characteristics:
    1. Not prime (prime numbers have exactly two divisors: 1 and itself)

    2. Greater than 1

    3. Can be factored into smaller positive integers


Examples:
    4: Divisors → 1, 2, 4

    6: Divisors → 1, 2, 3, 6

    9: Divisors → 1, 3, 9

    12: Divisors → 1, 2, 3, 4, 6, 12
    '''

n = int(input("Enter a number: "))
count = 0

for i in range (1, n + 1):
    if n % i == 0:
        count += 1
        
if count > 2 :
    print("Composite Number")
else:
    print("Not a Composite Number")