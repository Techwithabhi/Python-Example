class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other):
        if isinstance(other, Point):
            #isinstance used to check if object is instance
            return Point(self.x * other.x, self.y * other.y)
        
        else:
            return Point(self.x * other, self.y * other)
        
    def __rmul__(self, other):
        return Point(self.x * other, self.y * other)
    
    def __repr__(self):
        return ("{0},{1}".format(self.x,self.y))
    

p1 = Point(2, 3)
p2 = Point(3, 4)

print(p1 + p2)
print(p1 * p2)