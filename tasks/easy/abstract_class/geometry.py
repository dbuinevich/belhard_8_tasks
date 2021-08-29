"""
Описать класс Shape - фигура, у которого должно быть 2 абстрактных метода:
- get_perimeter для расчета периметра
- get_square для расчета площади

Описать класс Circle для круга, отнаследоваться от фигуры
добавить недостающие атрибуты
перегрузить методы get_perimeter и get_square
Длина окружности = 2 * pi * r
Площадь = pi * r ** 2

Описать класс Rectangle для прямоугольника, отнаследоваться от фигуры
добавить недостающие атрибуты
перегрузить методы get_perimeter и get_square
Периметр = 2 * a + 2 * b
Площадь = a * b


Описать класс Square для квадрата, отнаследоваться от прямоугольника
перегрузить методы get_perimeter и get_square
Периметр = 4 * a
Площадь = a ** 2
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_square(self):
        pass


class Circle(Shape):
    def get_perimeter(self, r: int):
        return 2 * pi * r

    def get_square(self, r: int):
        return pi * r ** 2


class Rectangle(Shape):
    def get_perimeter(self, a: int, b: int):
        return 2 * (a + b)

    def get_square(self, a: int, b: int):
        return a * b


class Square(Shape):
    def get_perimeter(self, a: int):
        return a * 4

    def get_square(self, a: int):
        return a ** 2


square = Square()
print(square.get_square(5))
print(square.get_perimeter(5))
