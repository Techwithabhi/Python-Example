## Check if a number is Harshad/Niven number. if the number is divisible by the sum of its digits.
'''
Example:
Take the number 18:

Sum of digits: 
1 + 8 = 9

Check divisibility: 
18 ÷ 9 = 2 (no remainder)

✅ So, 18 is a Harshad/Niven number.
'''

print("\nExample: 1\n")

n = 156
m = n 
sum = 0
prod = 1

while m != 0 :
    d = m % 10
    m = m // 10
    sum = sum + d
if n % sum == 0:
    print("YES")
else:
    print("NO")

print("\nExample: 2\n")

n = int(input("Enter a number: "))
sum = 0
org = n

while n != 0 :
    digit = n % 10
    n = n // 10
    sum += digit
if org % sum == 0 :
    print("Harshad number!")
else:
    print("Not a Harshad number!")