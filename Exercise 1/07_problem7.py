
## Writing FIBONACCI Series

'''
Fibonacci Sequence :- A famous mathematical sequence where each number is the sum of the two previous numbers.
Example:
Input = 7
Output = 0, 1, 1, 2, 3, 5, 8, 13, 21
'''

fib = [0, 1]
# Range starts from 0 by default

element = int(input("Enter a number: "))

n = element

for i in range(n):
    fib.append(fib[-1] + fib[-2])

# Convetrting the list of integers to string
print(', '.join(str(e) for e in fib))
