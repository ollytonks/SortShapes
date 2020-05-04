"""
    Simple object based system to generate a list of random 'shapes' 
    and sort them
"""
import random

class Triangle():
    def __init__(self):
        self.sides = 3
        self.corners = 3
    def __repr__(self):
        return "Triangle()"

class Quadrilateral():
    def __init__(self):
        self.name = "Quadrilateral"
        self.sides = 4
        self.corners = 4
    def __repr__(self):
        return "Quadrilateral()"

class Circle():
    def __init__(self):
        self.name = "Circle"
        self.sides = 1
        self.corners = 0
    def __repr__(self):
        return "Circle()"

def gen_shapes(n):
    """
    Take a number of objects to create and return a list of random shape objects
    """
    shapes = []
    for i in range(n):
        x = random.randint(0,2)
        if x == 0:
            shapes.append(Triangle())
        elif x == 1:
            shapes.append(Quadrilateral())
        else:
            shapes.append(Circle())
    return shapes

def shapeSort(shapes):
    """
    Take a list of shapes and sort it
    """
    circles = []
    quads = []
    triangles = []

    for shape in shapes:
        if shape.sides == 4:
            quads.append(shape)
        elif shape.sides == 3:
            triangles.append(shape)
        else:
            circles.append(shape)

    return circles, quads, triangles

def main():
    n = input("Number of shapes to generate: ")
    shapes = gen_shapes(int(n))
    print("\n")
    print(shapes)
    sort = input("Sort them? (y/n)")

    if sort == "y" or sort == "Y":
        circles, quads, triangles = shapeSort(shapes)
        print("\n---      All the Circles        ---")
        print(circles)
        print("\n---    All the Quadrilaterals   ---")
        print(quads)
        print("\n---      All the Triangles      ---")
        print(triangles)

if __name__ == "__main__":
    main()
