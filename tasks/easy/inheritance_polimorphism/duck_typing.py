"""
Создать 3 класса:

Cat, Duck, Cow

в каждом классе определить метод says()

Cat.says() - кошка говорит мяу
Duck.says() - утка говорит кря
Cow.says() - корова говорит муу


Написать функцию animal_says(), которая принимает объект и вызывает метод says
"""


class Animal:
    pass


class Cat(Animal):
    def says(self):
        print("кошка говорит мяу")


class Duck(Animal):
    def says(self):
        print("утка говорит кря")


class Cow(Animal):
    def says(self):
        print("корова говорит му")


def animal_says(animal):
    return animal.says()


animal = Cat()
animal_says(animal)
