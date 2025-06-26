## What is difference between class object and instance object?
'''
Class object is called only once, instance object can be called any no. of times.
Class object declared with class.objec
Instance object is declared with t1 = class(positional arguments) ane where the first argument is instance object(t1) implicity. Also int method is called impplicity after declaring instance object.
'''

class test:
    x = 20
    def __init__(self, a, b):
        self.a = a  # instance member argument
        self.b = b  # instance member argument
    def show(self):
        print(self.a, self.b)

print(test.x)   # class object 
t1 = test(4, 5) # instance object
t1.show()

# Displaying instance variable dirrectly
print(t1.a)
print(t1.b)
hgevgfdjasfdjy
