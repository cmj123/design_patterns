from enum import Enum 

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

# Define product class
class Product:
    def __init__(self, name, color, size):
        self.name = name 
        self.color = color 
        self.size = size 

# New requirement - we want to implement filter option by 1) colour, 2)Size, and 3) Color 
# First implementation - bad pattern
class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p 

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p 

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p

        #########
        # This is bad because
        # Leads to state space extension! Imagine 10 options 10 factorial!
        # for 3 criteria you have 7 methods - c s w cw sw  csw

        # OCP = open for extension and closed for modification
        

