## Print the following pattern.
'''
Z Z Z Z Z Z Z Z Z
  O O O O O O O 
    Z Z Z Z Z 
      O O O 
       Z Z
        O
'''
n = 6
for i in range(n):
    for j in range(i + 1):
        print(" ",end=" ")
    for j in range(i, n):
      
        if i % 2 == 0:
            print("Z", end=" ")
        else:
            print("O",end=" ")

    for j in range(i, n- 1):
      
        if i % 2 == 0:
            print("Z", end=" ")
        else:
            print("O", end=" ")

    print()
