from abc import ABC, abstractmethod
from math import pi as PI

class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return PI * (self.radius ** 2)


if __name__ == '__main__':
    square1 = Square(5)
    square1_area = square1.area()
    print(f"Square 1: side={square1.width}, area={square1_area}")

    square2 = Square(4)
    square2_area = square2.area()
    print(f"Square 2: side={square2.width}, area={square2_area}")

    rectangle1 = Rectangle(5, 3)
    rectangle1_area = rectangle1.area()
    print(f"Rectangle 1: width={rectangle1.width}, height={rectangle1.height}, area={rectangle1_area}")

    circle1 = Circle(2)
    circle1_area = circle1.area()
    print(f"Circle 1: radius={circle1.radius}, area={circle1_area}")

    circle2 = Circle(3)
    circle2_area = circle2.area()
    print(f"Circle 2: radius={circle2.radius}, area={circle2_area}")