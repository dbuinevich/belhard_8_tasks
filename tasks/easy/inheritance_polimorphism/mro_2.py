"""
Описать класс Device. Реализовать метод process_doc, который будет генерировать
raise NotImplementedError

Описать класс Scanner, который наследуется от Device. Реализовать метод
process_doc, который будет печатать "Сканирую документ: {name}"

Описать класс Copier, который наследуется от Device. Реализовать метод
process_doc, который будет печатать "Делаю копию: {name}"

Описать класс MFU, который наследуется от Scanner и Copier
Реализовать метод process_doc, который будет печатать "Сканирую, отправляю факс: {name}"

Создать объект класса MFU. Потренироваться вызывать методы через super,
через имя класса. Просмотреть MRO
"""


class Device:
    def process_doc(self):
        raise NotImplementedError


class Scanner(Device):
    def process_doc(self, name: str):
        print(f"Сканирую документ: {name}")


class Copier(Device):
    def process_doc(self, name: str):
        print(f"Делаю копию: {name}")


class MFU(Scanner, Copier):
    def process_doc(self, name: str):
        super(MFU, self).process_doc("hello")
        print(f"Сканирую, отправляю факс: {name}")

    @classmethod
    def new_classmethod(cls):
        print("this is classmethod")


small_mfu = MFU()
small_mfu.process_doc("important_doc")
print(MFU.mro())
MFU.new_classmethod()
