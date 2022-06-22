
# Problem 1

    # Distance formula
    # d = sqrt( (X2 - X1)^2 + (Y2 - Y1)^2 )

    # Slope fotmula
    # m = (Y2 - Y1) / (X2- X1)

class Line:
    
    def __init__(self,coor1,coor2):
        pass
    
    def distance(self):
        pass
    
    def slope(self):
        pass

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
    
    def __init__(self,height=1,radius=1):
        pass
        
    def volume(self):
        pass
    
    def surface_area(self):
        pass


c = Cylinder(2,3)

c.volume()

c.surface_area()
