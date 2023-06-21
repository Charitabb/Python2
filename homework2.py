class RectangularCoordinate:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
    def coordinate(self):
        return self.x, self.y
   
    def checkforaxis(self):
        return self.x == 0 or self.y == 0
    
    def checkforquadrant(self):
        if self.x == 0 or self.y == 0:
            return None
        if self.x > 0:
            if self.y > 0:
                return 'quadrant1'
            else:
                return 'quadrant4'
        elif self.x < 0:
            if self.y > 0:
                return 'quadrant2'
            else:
                return 'quadrant3'
    def distance_x(self):
        return abs(self.y)
    
    def distance_y(self):
        return abs(self.x)

    def distance_start(self):
        c = (abs(self.x))**2 + (abs(self.y))**2
        return c**0.5
        

    
my_coordinate = RectangularCoordinate(-3,-2)
print(my_coordinate.coordinate())
print(my_coordinate.checkforaxis())
print(my_coordinate.checkforquadrant())
print(my_coordinate.distance_x())
print(my_coordinate.distance_y())
print(my_coordinate.distance_start())
