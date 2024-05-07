
import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


choice = input("Enter Shape (circle, rectangle, triangle): ")

if choice.lower() == 'circle':
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)
    print("Circle area:", circle.area())

elif choice.lower() == 'rectangle':
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    rectangle = Rectangle(length, width)
    print("Rectangle area:", rectangle.area())


elif choice.lower() == 'triangle':
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    triangle = Triangle(base, height)
    print("Triangle area:", triangle.area())
else:
    print('Invalid Shape')

