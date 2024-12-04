import math

class Circle:
    def __init__(self, radius=0, diameter=0):
        if radius > 0:
            self.radius = radius
        elif diameter > 0:
            self.radius = diameter / 2
            
    def get_diameter(self):
        return self.radius * 2

    def set_diameter(self, value):
        if value > 0:
            self.radius = value / 2

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle with radius: {self.radius} and diameter: {self.get_diameter()}"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius

c1 = Circle(radius=8)
c2 = Circle(diameter=15)


print(c1)
print(f"Area of c1: {c1.get_area()}")
print(c2) 
print(f"Area of c2: {c2.get_area()}")


c1.set_diameter(12)
print(f"Updated c1: {c1}")


c3 = c1 + c2
print(c3)


print(c1 < c2)
print(c1 == c2)
print(c2 > c1)
