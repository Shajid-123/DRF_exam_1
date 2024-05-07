class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __mul__(self, other):
        if isinstance(other, Circle):
            return 3.14 * self.radius**2
        return NotImplemented

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __mul__(self, other):
        if isinstance(other, Rectangle):
            return self.length * self.width
        return NotImplemented

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def __mul__(self, other):
        if isinstance(other, Triangle):
            return 0.5 * self.base * self.height
        return NotImplemented

def calculate_area(shape):
    return shape * shape

def create_shape(shape_type):
    if shape_type == 'circle':
        radius = float(input("Enter the radius of the circle: "))
        return Circle(radius)
    elif shape_type == 'rectangle':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        return Rectangle(length, width)
    elif shape_type == 'triangle':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        return Triangle(base, height)
    else:
        return None

shape_type = input("Enter shape type (circle, rectangle, triangle): ")
shape = create_shape(shape_type)
if shape:
    print('Area:', calculate_area(shape))
else:
    print('Invalid Shape')
