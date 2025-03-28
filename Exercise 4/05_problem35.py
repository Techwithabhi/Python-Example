
## Is function overloading allowed in python?
'''
In python, function overloading as seen in languages like C++ or Java is not directly supported. However, Python provieds several ways to achieve similar behavior through default arguments, variable-length arguments, and more advance techniques like using functools.singledispatch. 

here are few methods to achive function overloading in Python:
'''

print('EXP - 1\n')

# 1. Using Default Arguments

# You can use default arguments  to provide defferent behavior based on the number of arguments passed

def greet(name, greeting = 'hello'):
    return f"{greeting}, {name}!"
print(greet('Abhi'))
print(greet('Jhon', "Hii"))

##############################################################################

print('\nEXP - 2\n')

# 2. Using veriable length Arguments

# You can use *args and **kwargs to accept a veriable number of arguments.

def add(*t):
    return sum(t)
print(add(1, 3))
print(add(1, 9, 2, 8, 6, 4))

##############################################################################

print('\nEXP - 3\n')

# 3. Using functools.singledispatch

# The functools.singledispatch decoretors allowes you to create a single-dispatch generic function, which can have different implementtations based on the type of the first argument.

from functools import singledispatch

@singledispatch
def process(value):
    raise NotImplementedError('Unsupported type')

@process.register(int)
def _(value):
    return f"Processing an integer: {value}"

@process.register(str)
def _(value):
    return f"Processing a string: {value}"

print(process(10))
print(process('Hello'))

##############################################################################

print('\nEXP - 4\n')

# 4. Using Class Methods

# You can also achiv overloading behavior using class methods.

class Math:
    @staticmethod
    def multiply(*t):
        result = 1
        for num in t:
            result *= num
        return result
    
print(Math.multiply(2, 3))
print(Math.multiply(2, 3, 7))
print(Math.multiply(2, 3, 7, 6, 1))