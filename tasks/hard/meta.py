"""
Создать метакласс, который будет фиксировать тип атрибута с помощью аннотаций.
При попытке присвоить атрибуту объект не подходящего типа сгенерировать исключение
ValueError
"""

#
# class MetaClass(type):
#     name: list
#     def __new__(mcs, name, bases, attrs):
#         if attrs[name] == type(name):
#         my_class = super().__new__(mcs, name, bases, attrs)
#         return my_class
