class Circle:
    def __init__(self, radius):
        self.radius = radius
    def __mul__(self):
        return 3.14 * self.radius ** 2
    
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def __mul__(self):
        return self.length * self.width
    
class Triangle:
    def __init__(self,base, height):
        self.base = base
        self.height = height
    def __mul__(self):
        return 0.5 * self.base * self.height
    

    
def area(shape):
    if shape == 'circle':
        r = int(input("Enter the radius of circle: "))
        area = Circle(r)
        return area.__mul__()
    elif shape == 'rectangle':
        l = int(input("Enter the length of rectangle: "))
        w = int(input("Enter the width of rectangle: "))
        area = Rectangle(l,w)
        return area.__mul__()
    elif shape == 'triangle':
        b = int(input("Enter the base of triangle: "))
        h = int(input("Enter the height of triangle: "))
        area = Triangle(b,h)
        return area.__mul__()
    else:
        return "Invalid Shape"

shape = input("Enter shape type(circle,rectangle,triangle): ")



print(f"Area: {area(shape)}")
