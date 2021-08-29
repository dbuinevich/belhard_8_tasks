"""
Написать класс Laptop (ноутбук), со следующими скрытыми атрибутами:

- cpu_cores - количество ядер процессора
- gpu_total - количество ГБ видеопамяти
- ram_total - количество ГБ ОЗУ

Определить методы:

- инициализатор __init__, с помощью которого присваиваются скрытые атрибуты
- метод can_play(game_name, cpu_cores, gpu_total, ram_total). Если требования игры
  меньше, чем характеристики компьютера, то вывести
  "На данном ПК есть возможность играть в {game_name}"
"""


class Laptop:
    __cpu_cores: int
    __gpu_total: int
    __ram_total: int

    def __init__(self, cpu_cores: int, gpu_total: int, ram_total: int):
        self.__cpu_cores = cpu_cores
        self.__gpu_total = gpu_total
        self.__ram_total = ram_total

    def can_play(self, game_name, cpu_cores, gpu_total, ram_total):
        if self.__cpu_cores >= cpu_cores and self.__gpu_total >= gpu_total and self.__ram_total >= ram_total:
            print(f"На данном ПК есть возможность играть в {game_name}")


new_game = Laptop(4, 8, 2)
new_game.can_play("game", 3, 7, 1)
