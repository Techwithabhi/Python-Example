## Check if a number is a special number. if sum of the digits plus product of the digits equal to the original number.

print("Example 1\n")

n = 59
m = n
sum = 0
prod = 1

while m != 0 :
    d = m % 10
    m = m // 10
    sum = sum + d ; prod = prod * d

if sum + prod == n:
    print("YES")
else:
    print("NO")



print("\nExample 2\n")


n = int(input("Enter a number: "))
sum_digits = 0
prod_digits = 1
original_number = n

while n != 0 :
    digit = n % 10
    n = n // 10
    sum_digits += digit
    prod_digits *= digit

if sum_digits == prod_digits:
    print(f"{original_number} is a spy number")
else:
    print(f"{original_number} is not a spy number")
