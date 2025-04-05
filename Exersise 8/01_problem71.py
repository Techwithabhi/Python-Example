## Print the following pattern.
'''
E D C B A
  E D C B
    E D C 
      E D 
        E
'''

n = 5

for i in range(n):
    p = 69
    for j in range(i + 1):
        print(" ",end=" ")
    for j in range(i, n):
        print(chr(p),end=" ")
        p -= 1
    print()