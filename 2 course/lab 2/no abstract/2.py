# Создать класс Фигура, в котором предусмотрены функции расчета площади и
# периметра геометрической фигуры. Создать дочерние классы для Круга,
# Четырехугольника (прямоугольник, квадрат, трапеция)
from math import pi, sqrt


class Figure():
    def __init__(self, *args):
        pass

    def area(self):
        pass

    def perimetr(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius**2

    def perimetr(self):
        return 2 * pi * self.radius


class Quadrangle(Figure):
    def __init__(self, *args):
        self.sides = args

    def perimetr(self):
        return sum(self.sides)


class Rectangle(Quadrangle):
    def __init__(self, length, width):
        super().__init__(length, width, length, width)

    def area(self):
        return self.sides[0] * self.sides[1]


class Square(Rectangle):
    def __init(self, side):
        super().__init__(side, side)


class Trapeze(Quadrangle):
    def area(self):
        a, c, b, d = self.sides
        return (a + b) / 2 * sqrt(
            c**2 - (((a - b)**2 + c**2 - d**2) / (2 * (a - b)))**2)
