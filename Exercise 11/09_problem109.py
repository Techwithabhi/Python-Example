## ## What are the commonly used decoretors in python?

class MyClass:
    class_vraiable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @staticmethod
    def static_method():
        print("This is a static method.")
        print("It doesn't have access to instance variables or self.")


# Using the static method without creating an instance
MyClass.static_method()