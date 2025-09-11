## Check if a number is Krishna Murthy special number or not. A number which is equal to the sum of factorial of its digits. eg. 145 = 1! + 4! + 5!
'''
Examples:
145
1! + 4! +5! = 1 +  + 120 = 145 ✅
So, 145 is a Krishna Murthy Number

1
1! = 1 ✅

2
2! = 2 ✅

40585
4! + 0! + 5! + 8! + 5! = 24 + 1+ 120 + 40320 + 120 = 40585 ✅
'''

import math

n = 145
m = n
sum = 0

while m != 0 :
    d = m % 10
    sum = sum + math.factorial(d)
    m = m // 10
    
if sum == n :
    print("YES")
else:
    print("NO")
