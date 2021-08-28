"""
Написать логгирующий декоратор, который все методы класса будет логгировать, т.е.
до выполнения функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}"
"""
import time


def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Выполнено {func.__name__}")
        return result
    return wrapper


def class_decorator(cls):
    functions = {key: value for key, value in cls.__dict__.items() if callable(value)}
    for key, value in functions.items():
        with_decorator = decorator(value)
        setattr(cls, key, with_decorator)
    return cls


@class_decorator
class Cat:
    def __init__(self, name: str):
        self.name = name

    def says(self):
        time.sleep(3)
        print(f"Котик {self.name} говорит МЯУ")


kotik = Cat("Рафонька")
kotik.says()
