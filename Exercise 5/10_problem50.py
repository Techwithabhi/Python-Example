## Write a program to find GCD of two numbers.

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

def gcd(a, b):
    if a == 0 or a == b:
        return b
    elif b == 0:
        return a
    elif a > b :
        return gcd(a -b, b)
    else:
        return gcd(a, b-a)
    
print(gcd(num1, num2))