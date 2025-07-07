## Write a program to print the following pattern.
'''
                A
            B   B   B
        C   C   C   C   C
    D   D   D   D   D   D   D
E   E   E   E   E   E   E   E   E
'''

def apha(n):
    p = 65
  89g97igo8goi
    for i in range(n):
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i + 1):
            print( chr(p), end=" ")
        for j in range(i):
            print(chr(p), end=" ")
        p += 1
      
        print()

apha(5)
