## Check if a number is automorphic number or not. it is a number which is contained in the last digit(s) of its square. eg. 25 in 625.
'''
Exapmles:
    Take = 5
    Square of 5 = 25
    Ends with 5 → ✅ Automorphic

    Take = 76
    Square of 76 = 5776
    Ends with 76 → ✅ Automorphic

    Take = 25
    Square of 25 = 625
    Ends with 25 → ✅ Automorphic

    Take = 7
    Square of 7 = 49
    Does not end with 7 → ❌ Not Automorphic
'''

# n = 25

n = 9
m = n
q = n*n
 
while m != 0 :
    d = m % 10; d1 = q % 10
    if d != d1 : flag = 1
    m = m // 10 ; q = q // 10
if flag == 0:
    print("YES")
else:
    print("NO")