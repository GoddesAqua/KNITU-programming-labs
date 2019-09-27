from math import sqrt, isclose


def distance(A, B):
    return sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)


def is_rectangle(coords):
    A, B, C, D = coords[0], coords[1], coords[2], coords[3]
    is_equale = isclose(distance(A, B), distance(C, D))
    is_angle = isclose(
        distance(A, C)**2,
        distance(A, B)**2 + distance(A, D)**2
    )
    return (is_equale and is_angle)


class Rectangle:
    def __init__(self, coords):
        if all(
                all(
                    0 <= coord <= 20 and type(coord) is float
                    for coord in vertex
                ) for vertex in coords
        ) and is_rectangle(coords):
            self.coords = coords
        else:
            print(
                'Ошибка, числа должны быть типа float, '
                'находится между 0 и 20 и описывать прямоугольник'
            )

    def A(self):
        return self.coords[0]

    def B(self):
        return self.coords[1]

    def C(self):
        return self.coords[2]

    def D(self):
        return self.coords[3]

    def length(self):
        return max(distance(self.A(), self.B()), distance(self.B(), self.C()))

    def width(self):
        return min(distance(self.A(), self.B()), distance(self.B(), self.C()))

    def perimetr(self):
        return (self.width() + self.length()) * 2

    def area(self):
        return self.width() * self.length()

    def square(self):
        return (self.length() == self.width())


if __name__ == '__main__':
    user_coords = [list(map(float, input().split())) for i in range(4)]
    user_rectangle = Rectangle(user_coords)
    print(
        user_rectangle.perimetr(),
        user_rectangle.area(), user_rectangle.square()
    )
