## What are the commonly used decoretors in Python?

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Getter method for radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter method for radius"""
        if value < 0:
            raise ValueError("Value cannot be negative")
        self.radius = value

    @property
    def area(self):
        """Method to calculate the area"""
        return 3.14 * self._radius**2
    
#Creating instance of circle class
obj = Circle(radius=5)

print(f"radius:{obj.radius}")

print(f"area:{obj.area}")