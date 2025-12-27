## Check if a number is palindrome or not.
'''
A palindrome number is a number that remains the same when its digits are reversed. In other words, it reads the same forward and backward.

Examples:
    121 → Reverse: 121 (Palindrome)

    1331 → Reverse: 1331 (Palindrome)

    123 → Reverse: 321 (Not a palindrome)
'''

print("Example 1\n")

#Initialization

n = 12321
m = n
sum = 0

while m != 0:
    # logic
    d = m % 10
    sum = sum*10+d
    m = m//10
# check if true or not
if sum == n:
    print("YES")
else:
    print("NO")



print("\nExample 2\n")

# Take input from the user
n = int(input("Enter a N=number: "))

# Store the original number
original_number = n

# Initialize sum to build the reversed number
reversed_number = 0

# Reversed the number
while n != 0:
    digit = n % 10
    reversed_number = reversed_number * 10 + digit
    n = n // 10

# Check if the reversed number matches the original number
if reversed_number == original_number:
    print("YES")
else:
    print("NO")
