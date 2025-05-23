## Write a program to print the following pattern.
'''
       A
      A B
    A  B  C
  A  B  C  D
 A  B  C  D  E 
'''

def apha(n):
    num = 65
    for i in range(n):
        for j in range(i, n):
            print(" ", end="")
        for j in range(i + 1):
            print(chr(num), end=" ")
            num += 1
        num = 65
        print()
apha(5)
