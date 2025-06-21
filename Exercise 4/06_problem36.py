
# What are positional argument in python?

'''
There are two types of arguments in python, positional arguments and keyword arguments. keyword arguments are assigned with the keywords that are define with the function. Keyword arguments should always be declared after the positional arguments.
'''

def f1 (a, b):
    print("a =", a,", b =" , b)

f1(3, 5)# Positional argument
# f1(b = 30, 5) # Syntax error(compile time error)

f1(30,b= 4)
# f1(2, a = 10) # type error : multiple values of a (run time error)

f1(a = 23, b = 34) # Keyword argument

trcufu6yfyuf
