## What are the commonly used decoretors in python?

# static method calculator code

class Calculator:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
        return x - y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def divide(x, y):
        if y != 0:
            return x / y
        else:
            print("Cannot divied by zero.")
            return None
        
# Using the statick methods without creating an instance
result_add = Calculator.add(50, 13)
print(f"Addition: {result_add}")

result_subtract = Calculator.subtract(80, 43)
print(f"Subtraction: {result_subtract}")

result_multiply = Calculator.multiply(20, 6)
print(f"Multiplication: {result_multiply}")

result_divied = Calculator.divide(100, 2)
print(f"Division: {result_divied}")
