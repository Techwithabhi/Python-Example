## Print the following pattern.
'''
R E D O C
  E D O C
    D O C
      O C
        C
'''

s = "CODER"
n = len(s)
k = n - 1

for i in range(n):
    p = k
    for j in range(i + 1):
        print(" ",end=" ")
    for j in range(i, n):
        print(s[p],end=" ")
        p -= 1
    print()
    k -= 1