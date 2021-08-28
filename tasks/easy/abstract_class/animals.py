"""
Описать абстрактный класс Animal со следующими атрибутами:

- name - кличка
- a_type - домашнее или дикое

и абстрактным методом says()

На основе Animal определить классы Cat, Dog, Cow, которые переопределят метод says,
чтобы он выводил, например "Кошка {name} говорит МЯУ"
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    name: str
    a_type: str

    @abstractmethod
    def says(self, name: str):
        pass


class Cat(Animal):

    def says(self, name: str):
        print(f"Котик {name} говорит МЯУ")


class Dog(Animal):

    def says(self, name: str):
        print(f"Собака {name} говорит ГАВ")


class Cow(Animal):

    def says(self, name: str):
        print(f"Корова {name} говорит МУ")


kotik = Cat()
kotik.says('Рафонька')
