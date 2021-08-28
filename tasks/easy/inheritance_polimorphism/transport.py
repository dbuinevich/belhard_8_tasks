"""
Описать класс Transport, у которого следующие атрибуты:

- brand - фирма, выпустившая транспорт
- model - модель
- issue_year - год выпуска
- color - цвет

Определить методы:

- move - который делает raise NotImplementedError

Описать класс Car, который наследуется от Transport, у которого следующие атрибуты:

- mileage - пробег
- engine_type

Определить методы:

- move - который принимает количество километров, увеличивает на это количество пробег
  и печатает "{brand} {model} проехала {km} километров"

Описать класс Airplane, который наследуется от Transport, у которого следующие атрибуты:

- mileage - пробег
- lifting_capacity - грузоподъемность

Определить методы:

- move - который принимает количество километров, увеличивает на это количество пробег
  и печатает "{brand} {model} пролетел {km} километров"
"""


class Transport:
    brand: str
    model: str
    issue_year: int
    color: str

    def __init__(self, brand: str, model: str, issue_year: int, color: str):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.color = color

    def move(self):
        raise NotImplementedError


class Car(Transport):
    mileage: int
    engine_type: str

    def __init__(self, mileage: int, engine_type: str):
        super(Car, self).__init__('brandik', 'modelka', 2021, 'black')
        self.mileage = mileage
        self.engine_type = engine_type

    def move(self, km: int):
        self.mileage = self.mileage + km
        print(f"{self.brand} {self.model} проехала {km} километров")


class Airplane(Transport):
    mileage: int
    lifting_capacity: int

    def __init__(self, mileage: int, engine_type: str):
        super(Airplane, self).__init__('brandik', 'modelka', 2021, 'black')
        self.mileage = mileage
        self.engine_type = engine_type

    def move(self, km: int):
        self.mileage = self.mileage + km
        print(f"{self.brand} {self.model} пролетел {km} километров")


car = Car(25, "mashinka")
car.move(50)
print(car.mileage)
plane = Airplane(25000, 'samoletik')
plane.move(50000)
