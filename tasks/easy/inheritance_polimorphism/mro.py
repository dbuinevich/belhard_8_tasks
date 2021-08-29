"""
Описать класс Cars. Реализовать метод print_fuel_type, который будет генерировать
raise NotImplementedError

Описать класс PetrolMotorCars, который наследуется от Cars. Реализовать метод
print_fuel_type, который будет печатать "Бензин"

Описать класс ElectricMotorCars, который наследуется от Cars. Реализовать метод
print_fuel_type, который будет печатать "Электричество"

Описать класс HybridCars, который наследуется от PetrolMotorCars и ElectricMotorCars
Реализовать метод print_fuel_type, который будет печатать "Бензин + электричество"


Создать объект класса HybridCars. Потренироваться вызывать методы через super,
через имя класса. Просмотреть MRO
"""


class Cars:
    def print_fuel_type(self):
        raise NotImplementedError


class PetrolMotorCars(Cars):
    def print_fuel_type(self):
        print("Бензин")


class ElectricMotorCars(Cars):
    def print_fuel_type(self):
        super(ElectricMotorCars, self).print_fuel_type()
        print("Электричество")


class HybridCars(PetrolMotorCars, ElectricMotorCars):
    def print_fuel_type(self):
        super(HybridCars, self).print_fuel_type()
        print("Бензин + электричество")

    @classmethod
    def class_method(cls):
        print("this is a method for the whole HC class")


hybrid = HybridCars()
hybrid.print_fuel_type()
print(HybridCars.mro())
HybridCars.class_method()
