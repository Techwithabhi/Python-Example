## Print the following pattern.
'''
          E
        D E D
      C D E D C 
    B C D E D C B 
  A B C D E D C B A        
'''

n = 5
k = 69
for i in range(n):
    p = k
    for j in range(i, n):
        print(" ",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
        p += 1
    for j in range(i + 1):
        print(chr(p),end=" ")
        p -= 1
    k -= 1
    print()