## Check if a number is duck number or not. Number which has zeros present in it.
'''
A Duck Number is a positive number that contains at least one zero, but does not start with zero.

Example:

    1023 → ✅ Duck number (has a zero, not at the start)

    089 → ❌ Not a Duck number (starts with zero)

    4005 → ✅ Duck number (zero is not leading)

'''

n = 100120
m = n
count = 0

while m != 0 :
    d = m % 10
    m = m // 10
    if d == 0 : 
        count += 1
if count > 0 :
    print("YES")
else:
    print("NO")
print("No of zeros in number: ",count)