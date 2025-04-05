
## Write a proogram to print the following pattern.
'''
    *
    *   *
    *   *   *
    *   *   *   *
    *   *   *   *   *
'''

s = int(input("Enter a number: "))

for i in range(1, s+1):
    print("*  " * i)
    i += 1