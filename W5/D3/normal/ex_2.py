from hmac import new
import math
from turtle import circle
from xml.etree.ElementTree import PI
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the circle and get something nice
# Be able to add two circles together
# Be able to compare two circles to see which is bigger
# Be able to compare to see if there are equal
# Be able to put them in a list and sort them




class Circle():
    LIST = []
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            try:
                if k == "radius":
                    self.radius = v
                    self.diameter = self.radius*2
                elif k == "diameter":
                    self.radius = v/2
                    self.diameter = v
                elif k == "circumference":
                    self.radius = v/(math.pi*2)
                    self.diameter = self.radius*2
            except ValueError:
                raise ("There is an issue with your arguments!")

    def __str__(self):
        return f"This circle has the following attributes: {__name__}\n Radius: \t\t\t\t {self.radius}\n Diameter: \t\t\t\t {self.diameter}\n Area: \t\t\t\t\t {self.area()}"\

    def __eq__(self, other):
        equal = False
        if self.area() == other.area():
            equal = True 
        return equal

    def __lt__(self, other):
        lt = False
        if self.area() < other.area():
            lt = True
        return lt

    def __le__(self, other):
        le = False
        if self.area() <= other.area():
            le = True
        return le

    def __ge__(self, other):
        ge = False
        if self.area() >= other.area():
            ge = True
        return ge

    def __gt__(self, other):
        gt = False
        if self.area() > other.area():
            gt = True
        return gt

    def sort_by_size(self, other):    
        Circle.LIST.append(self)
        Circle.LIST.append(other)
        
        for circle in range(len(Circle.LIST)-1):
            if Circle.LIST[circle].area() < Circle.LIST[circle+1].area():
                tmp = Circle.LIST[circle+1]
                Circle.LIST[circle+1] = Circle.LIST[circle]
                Circle.LIST[circle] = tmp
        return Circle.LIST

    def area(self):
        """
        calculates area of a circle
        """
        circle_area = math.pi * self.radius**2
        return round(circle_area, 2)

    

    
    

def main():
    newCircle = Circle(radius= 5)
    # print(newCircle.radius)
    print(f"The circle has the area of: \t\t {newCircle.area()}")
    print(newCircle)
    secondCircle = Circle(circumference = 10)
    print(secondCircle.radius)
    print(secondCircle == newCircle)    
    print(secondCircle > newCircle)
    Circle.sort_by_size(newCircle,secondCircle)
    for circle in Circle.LIST:
        print(circle.area())
    print(Circle.LIST)
if __name__ == "__main__":
    main()
