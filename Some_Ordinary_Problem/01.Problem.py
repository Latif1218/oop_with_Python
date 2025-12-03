# Define a Circle class to create a circle with radius r using the constructor
# Defile an Area() method of the class which calculate the area of the circle 
# Define a Parimeter() method of the class which allows you to calculate the perimeter of the circle


class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def Area(self):
        circleArea = 3.1416*self.radius**2
        return circleArea
    
    def Perimeter(self):
        circlePerimeter = 2*3.1416*self.radius
        return circlePerimeter
    

c2 = Circle(21)
print(c2.Area())
print(c2.Perimeter())