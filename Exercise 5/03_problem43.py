## What are default argument in functions?
'''
The arguments that are declared and assigned a value while creating a function are called default arguments.

It is not allowed to have non-default arguments after default arguments.
'''

def add(a, b, c = 5):   # c is default argument
    return a + b + c

s = add(2, 3)
print('The addition is :',s)
