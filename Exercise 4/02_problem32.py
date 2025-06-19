
## What is Python decoretor ?

print('EXP - 1\n')
# Functio decoretor

def welcome(fx):
    def mfx(*t, **d):
        print("Before hello function")
        fx(*t, **d) # *args to make arguments as tuple, **kwags to take arguments 
        print("Thanks for using the function")
    return mfx

# decoretor function without arguments
@welcome
def hello():
    print("Hello !")

# decoretor function with arguments
@welcome
def add(a,b):
    print(a+b)

hello()
add(1, 3)
fcycvtyuvcutyc
##############################################################################

print('\nEXP - 2\n')
# Class Decoretor

class Calculator:
    def __init__(self,func):
        self.function = func

    def __call__(self, *t, **d):
        result = self.function(*t, **d)
        return result**2
    
@Calculator
def add(a, b):
    return a + b

# add = Calculator(add)
result = add(10, 50)  # add.__call__(a, b) since function type is callable
print(result)

#############################################################################

print('\nEXP - 3\n')
# Decoretors are used to modify the behavior of function or methods without changing their code.
# Decoretors functions is a functions that takes another functions as their argument.

def decor_result (result_function):
    def distinction(marks):
        results = []  # List to store result for each element
        for m in marks:
            if m >= 75:
                print('DISTINCTION')
            results.append(result_function([m]))  # pass a list with the current element
        return results # return the collected results
    return distinction

@decor_result
def result(marks):
    for m in marks:
        if m >= 33:
            pass
        else:
            print('FAIL')
            return "FAIL"  #return FAIL if any element fails
        
    else:
        print('PASS')
        return "PASS"   # return PASS if all elements pass
    

# Get the results for each elements 
results = result([45, 78, 80, 25, 66, 91, 31])


print("results:", results)
