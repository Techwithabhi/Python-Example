## Print the following pattern.
'''
          A
        B C D 
      E F G H I 
    J K L M N O P
  Q R S T U V W X Y        
'''
n = 5
p = 65

for i in range(n):
    for j in range(i, n):
        print(" ",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
        p += 1
    for j in range(i + 1):
        print(chr(p), end=" ")
        p += 1
    print()
