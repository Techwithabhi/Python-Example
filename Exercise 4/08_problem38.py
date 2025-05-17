## How to create static member variables in class?

'''
static variables are shared among all instences of a class and are typically used to store class-level data.

Class Method: use @classmethod when you need too access or modify the class state or call the method on the class itself. Static Method: Use @staticmethod utility functions that don't need to access or modify class or instance state but logically belong to the class.

Static method are method that are bound to a class rather then an intance and do not have access to intance-specific data. To declare a static method, use @staticmethod decorator befor defining the method.

Use Case: Static method are typically used for utility function that perform a task in isolation and do not need to access or modify class or intance data.

Static veriables: a is defined as a static veriable directly within the class body. b, c, d, e, and f are also static variables, but they are deffined within methods. g is defined as a static variable outside the class body.

Instance Variable: x is as instance veriable, initialized within the init method.

local Veriables: y is local variable, initialized within the init method. it is only accessible within this method.
'''

class myclass:
    a = 5   # static variable
    def __init__(self):
        self.x = 10
        y = 4   # instance variable - can be used anywhere in class using self
        myclass.b = 34  # static variable
    def f1(self):
        myclass.c = 65  # static veriable 
    @staticmethod
    def f2 (self):
        myclass.d = 66  # static veriable 
    @classmethod
    def f3 (cls):
        cls.e = 15   # static veriable 
        myclass.f = 53   # static veriable 
myclass.g = 11   # static veriable 

print(myclass)


hi 



