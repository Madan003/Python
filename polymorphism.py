class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def calculate_area(self):
        print(f"The area of circle is: {3.14*self.radius**2}")

class Rectangle(Shape):
    def __init__(self,l,w):
        self.len = l
        self.wid = w

    def calculate_area(self):
        print(f"The area of rectangle is: {self.len*self.wid}")

#normal
c = Circle(5)
r = Rectangle(6,4)
c.calculate_area()
r.calculate_area()

#looping
areas = [Circle(5),Rectangle(6,4)]
for area in areas:
    area.calculate_area()