class Rectangle:
    def __init__(self, width, height) -> None:
        self._width = width 
        self._height = height

    @property
    def area(self):
        return self._width *self._height

    def __str__(self) -> str:
        return f"Width: {self.width}, height: {self.height}"

    @property
    def width(self):
        return self._width 

    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        self._height

    @height.setter 
    def height(self, value):
        self._height = value

class Square(Rectangle):
    def __init__(self, size) -> None:
        super().__init__(size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value 

    @Rectangle.height.setter
    def height(self, value):
        self._height = self._width = value 

def use_it(rc):
    w = rc.width 
    rc.height = 10 
    expected = int(w*10)
    print(f'Expected an area of {expected}, got {rc.area}')

rc = Rectangle(2, 3)

use_it(rc)


# sq = Square(5) # Violates Liskov Substitution Principle

# You dont need a square class. Alternatively use 
sq = Rectangle(5,5)

use_it(sq)

