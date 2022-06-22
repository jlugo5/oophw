
# Problem 1

    # Distance formula
    # d = sqrt( (X2 - X1)^2 + (Y2 - Y1)^2 )

    # Slope fotmula
    # m = (Y2 - Y1) / (X2- X1)

import math
    
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        return math.sqrt( (self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2 )
    
    def slope(self):
        return ( (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0]) )

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

li.distance()

li.slope()


# Problem 2

    # volume 
    # v = pi * r^2 * h

    # surface area
    # a = 2 * pi * r * h + 2 * pi * r^2

class Cylinder:
    
    pi = 3.14
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return ( pi * self.radius**2 * self.hieght )
    
    def surface_area(self):
        return ( 2 * pi * self.radius * self.height + 2 * pi * self.radius**2 )


c = Cylinder(2,3)

c.volume()

c.surface_area()
