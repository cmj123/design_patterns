
from enum import Enum

from enum import Enum 
from math import *

class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2

class Point:
    # Case 1
    # # Cant have two initalisers
    # def __init__(self, x,y) -> None:
    #     self.x = x 
    #     self.y = y 

    # def __init__(self, rho, theta) -> None:
    #     self.rho = rho 
    #     self.theta = theta

    # Case 2
    # # # Let use a coordinate system
    # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN) -> None:
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b 
    #     elif system ==  CoordinateSystem.POLAR:
    #         self.x = a * cos(b)
    #         self.y = a * sin(b)

    #     ## The problem with using this method is  that when you have a new coordinate syste
    #     ## You have to update the Class CoordinateSystem and add a new if case to the __init__ function
    #     ## Break the open close principle
    #     ## Maps hard.... what's a? what's b?

    # Case 3
    # Facrtor in its simplest form is anoything that creates an object usually for initialisation
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    

    def __str__(self) -> str:
        return f'x: {self.x}, y: {self.y}'

    class PointFactory:
        @staticmethod
        def new_cartesian_point(x,y):
            return Point(x,y)

        @staticmethod
        def new_polar_point( rho, theta):
            return Point(rho * sin(theta), rho * cos(theta))

    # Introducing singleton
    factory = PointFactory()

class PointFactory:
    @staticmethod
    def new_cartesian_point(x,y):
        return Point(x,y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * sin(theta), rho * cos(theta))

if __name__ == "__main__":
    p = Point(2,3)
    p2 = Point.factory.new_cartesian_point(1,2)
    p3 = Point.factory.new_polar_point(1,7)

    print(p)
    print(p2)
    print(p3)

