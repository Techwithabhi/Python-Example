## What is name mingling in python? 
'''
When a veriable is initialize with double underscore, its name is automatically change in python to_class_variableName. This phenomenon is called Name Mingling in python.

Name mangling is a technique useed in programing to generate unique names for entities like functions and variables to avoid name colisions. this is especally importent in languages with features like function overloading and namespaces. The main purposes of name mangling are:

1. Avoiding Name Collisions: Ensures unique names for entities with the same name in different scopes or modules.

2. Supporting Function Overloading: Encodes function names with parameter types to differentiate overloading function.
'''

class world:
    x = 10

    __india = 20

print(world.x)
print(world._world__india)


