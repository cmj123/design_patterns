# pylint: disable=too-few-public-methods
# pylint: disable=arguments-differ
"Prototype Concept Sample Code"

from abc import ABCMeta, abstractmethod

class IProtoType(metaclass=ABCMeta):
    "Interface with clone, deep or shallow."

    @staticmethod
    @abstractmethod
    def clone():
        """ The clone, deep or shallow.
        It is up to you how you want to implement
        the details in your concrete class
        """

class MyClass(IProtoType):
    "A concrete class"

    def __init__(self, field):
        self.field = field # any value of type 

    def clone(self):
        "This clone method uses a shallow copy technique"
        return type(self)(
            # self.field
            self.field.copy()
        )
    
    def __str__(self) -> str:
        return f"{id(self)}\tfield={self.field}\ttype={type(self)}"
    
# The Client
OBJECT1 = MyClass([1,2,3,4]) # Create the object containing a list 
print(f"OBJECT1{OBJECT1}")

OBJECT2 = OBJECT1.clone()

OBJECT2.field[1] = 101 

# Comparing OBJECT1 and OBJECT2 
print(f"OBJECT2 {OBJECT2}")
print(f"OBJECT1 {OBJECT1}")
