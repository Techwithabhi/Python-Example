## Check if a number is spy number. Means sum of its digits equal to the product of its digits.
'''
Example:
    112

        Sum of digits: 1 + 1 + 2 = 4

        Product of digits: 1 x 1 x 2 = 2

        Since 4 ≠ 2, it is not a Spy Number.

    123

        Sum of digits: 1 + 2 + 3 = 6

        Product of digits: 1 x 2 x 3 = 6

        Since 6 = 6, 123 is a Spy Number.
'''
n = 132
m = n
sum = 0
prod = 1

while m != 0 :
    d = m % 10
    m = m // 10
    sum = sum + d
    prod = prod * d 

if sum == prod:
    print("YES")
else:
    print("NO")