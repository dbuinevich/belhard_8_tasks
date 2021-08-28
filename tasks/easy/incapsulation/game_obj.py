"""
Напишите класс GameObject, в котором будут храниться координаты объекта.

- x int
- y int

Координаты должны быть доступны для чтения, а их изменение должно происходить в методе
move(delta_x, delta_y)

реализовать через property
"""


class GameObject:
    __x: int
    __y: int

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def сhanged_x(self):
        return self.__x

    @property
    def сhanged_y(self):
        return self.__y

    def move(self, delta_x, delta_y):
        self.__x = self.__x + delta_x
        self.__y = self.__y + delta_y


obj = GameObject(25, 25)
obj.move(-5, 5)
print(obj.сhanged_y)
print(obj.сhanged_x)
