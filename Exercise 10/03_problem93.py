## Check if the number is Neon number. Number, digits of whose sueare are equal to the number itself.
'''
Example:

    Take n = 9
    Square of 9 = 81
    8 + 1 = 9 ✅ So, 9 is a Neon Number

    Take n = 1
    square of 1 = 1
    1 = 1 ✅ Also a Neon Number

    Take n = 7
    Square of 7 = 49
    4 + 9 = 13 ❌ Not a Neon Number
'''

n = 9
m = n ** 2
sum = 0

while m != 0 :
    d = m % 10
    sum = sum + d
    m = m // 10
    
if sum == n :
    print("YES")
else:
    print("NO")
