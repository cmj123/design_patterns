# pylint: disable=too-few-public-methods
"FactorB Sample Code"
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
    
class FactoryB:
    "The Factory Class"

    @staticmethod
    def create_object(some_property):
        "A static method to get a concrete product"
        try:
            if some_property == 'a':
                return ConcreteProductA()
            if some_property == 'b':
                return ConcreteProductB()
            if some_property == 'c':
                return ConcreteProductC()
            raise Exception('Class Not Found')
        except Exception as _e:
            print(_e)
        return None 