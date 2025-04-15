## What are the commonly used decoretors in python?
'''
Some commonly used decoretors that are built into Python are @classmethod, @staticmethod

@classmethod decoretors often used for operations that involve class and its
'''

class Myclass:
    a = "I am a class variable"

    def __init__(self,len):
        self.length = len

    @classmethod
    def class_method(cls):
        print("This is a class method.")
        print(f"using class veriable: {cls.a}")


#using class method without creating an instance
Myclass.class_method()