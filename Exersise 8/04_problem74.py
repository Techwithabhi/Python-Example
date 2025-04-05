## Print the following pattern.
'''
        A
      A B A
    A B C B A
  A B C D C B A
A B C D E D C B A 
'''
n = 5
for i in range(n):
    p = 65
    for j in range(i, n):
        print(" ",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
        p += 1
    for j in range(i + 1):
        print(chr(p),end=" ")
        p -= 1
    print()