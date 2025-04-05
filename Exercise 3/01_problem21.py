## Create a generator to produce first n numbers?

print('EXE : 1')

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_generator(n):
    num = 2
    while n:
        if isPrime(num):
            yield num
            n -= 1  # Correct decrement
        num += 1  # Correct increment

'''
1. yield keyword used to return a value and then the code is resumed inside the function unlike the return keyword end the code when it is called 

2. yield keyword will turn any expression that is hiven with it into a generator object and return it to the caller
'''

x = int(input("Enter no. of Prime numbers required: "))
it = prime_generator(x)

for e in it:
    print(e, end=" ")


## Program to check if a given number is prime or not?

print('EXE : 2')

def prime_no(n):
    Flag = False

    if n < 2:
        return Flag
    else:
        for i in range(2, n):
            if n % i == 0:
                return Flag
            else:
                flag = True
                return flag
            
num = int(input("Enter a number: "))

print(prime_no(num))
