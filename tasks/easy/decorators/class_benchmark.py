"""
Написать декоратор, который будет проводить бенчмарк всех методов класса.

До выполнения метода будет печатать:
Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}
Время начала: {start_time}

После выполнения метода будет печатать:
Выполнено {func.__name__}
Время окончания: {end_time}
Всего затрачено времени на выполнение: {end_time - start_time}
"""
import time

# start_time = time.time()
# end_time = time.time()
# difference = e - s


def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}")
        print(f"Время начала: {start_time}")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Выполнено {func.__name__}")
        print(f"Время окончания: {end_time}")
        print(f"Всего затрачено времени на выполнение: {end_time - start_time}")
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
