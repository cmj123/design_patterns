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

# Specification - base class

class Specification:
    '''
    Base class for specification
    '''
    def is_satifised(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

class Filter:
    '''
    Base class for filter
    '''
    def filter(self, items, spec):
        pass 

class ColorSpecification(Specification):
    '''
    Class for color specification
    '''
    def __init__(self, color):
        self.color = color 

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    '''
    Class for color specification
    '''
    def __init__(self, size):
        self.size = size 

    def is_satisfied(self, item):
        return item.size == self.size 

class AndSpecification(Specification):
    def __init__(self, *args) :
        self.args = args 

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item 

if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    pf = ProductFilter()
    print('Green products (old):')
    # for p in  pf.filter_by_color(products, Color.GREEN):
    #     print(f' - {p.name} is green')

    # Better Filter
    bf = BetterFilter()

    # print('Green products (new):')
    green = ColorSpecification(Color.GREEN)
    # for p in bf.filter(products, green):
    #     print(f' - {p.name} is green')

    # print('\nLarge products:')
    large = SizeSpecification(Size.LARGE)
    # for p in bf.filter(products, large):
    #     print(f' - {p.name} is large')

    print('Large green items:')
    # large_green = AndSpecification(large, green)
    large_green = large & green 
    for p in bf.filter(products, large_green):
        print(f' - {p.name} is large')

    

    

        

