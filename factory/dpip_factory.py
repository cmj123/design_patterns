# The Factor Concept
from abc import ABCMeta, abstractmethod

class IProduct(metaclass=ABCMeta):
    "A hypothetical class interface (Product)"

    @staticmethod
    @abstractmethod
    def create_object():
        "An abstract interface method"
        pass

class ConcreteProductA(IProduct):
    "A concrete class that implements the IProduct Interface"

    def __init__(self) -> None:
        self.name = "ConcreteProductA"

    def create_object(self):
        return self
    
class ConcreteProductB(IProduct):
    "A concrete class that implements the IProduct Interface"

    def __init__(self) -> None:
        self.name = "ConcreteProductB"

    def create_object(self):
        return self
    
class ConcreteProductC(IProduct):
    "A concrete class that implements the IProduct Interface"

    def __init__(self) -> None:
        self.name = "ConcreteProductC"

    def create_object(self):
        return self
    
class Creator:
    "The Factory Class"

    @staticmethod
    def create_object(some_property):
        "A static method to get a concrete product"
        if some_property == 'a':
            return ConcreteProductA()
        if some_property == 'b':
            return ConcreteProductB()
        if some_property == 'c':
            return ConcreteProductC()
        return None 
    
# The Client
PRODUCT = Creator.create_object('b')
print(PRODUCT.name)