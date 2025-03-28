## Write a program to print the following pattern.
'''
        A
       B C
      D E F
     G H I J
    K L M N O 
'''

def apha(n):
    num = 65
    for i in range(n + 1):
        for j in range(n - i):
            print(" ",end="")
        for j in range(1, i + 1):
            print(chr(num),end=" ")
            num += 1
        print("")

apha(5)