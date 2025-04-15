## Create the following pattern.
'''
    5  4  3  2  1
       4  3  2  1
          3  2  1
             2  1
                1
'''

n = 5
p = 5

for i in range(n):
    k = p
    for j in range(i + 1):
        print(" ",end=" ")
    for j in range(i, n):
        print(k, end=" ")
        k -= 1
    p -= 1
    print()