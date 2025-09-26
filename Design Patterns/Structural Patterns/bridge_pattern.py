from abc import ABC, abstractmethod
#------------Implementor----------
class Color(ABC):
    @abstractmethod
    def fill(self):
        pass

#--------------Concrete Implementors-----------
class Red(Color):
    def fill(self):
        return "Red"

class Blue(Color):
    def fill(self):
        return "Blue"

#--------------Abstraction--------------
class Shape(ABC):
    def __init__(self, color:Color):
        self.color = color
    
    def draw(self):
        pass

#----------Refined Abstraction------------
class Circle(Shape):
    def draw(self):
        print(f"Drawing circle is {self.color.fill()} color")


class Square(Shape):
    def draw(self):
        print(f"Drawing Square in {self.color.fill()} color")
        
red = Red()
circle = Circle(red)
circle.draw()