"""
Определить класс Person с атрибутами:

- fio - ФИО
- phone - номер телефона

Описать класс LibraryReader, который наследуется от Person c атрибутами:

- id - номер читательского билета
- books - список книг

Определить методы:

- инициализатор __init__
- take_book(*args) - принимает произвольное количество книг и выводит сообщение:
  "Петров В. В. взял книги: Приключения, Словарь, Энциклопедия", если взято до 3 книг, и
  "Петров В. В. взял 4 книги", если больше

- return_book(*args) - принимает произвольное количество книг и выводит сообщение:
  "Петров В. В. вернул книги: Приключения, Словарь, Энциклопедия", если вернул до 3 книг
  и "Петров В. В. вернул 4 книги". Если какой то книги нет, то выводится сообщение
  "Петров В. В. не брал Рассказы"
"""


class Person:
    fio: str
    phone: str


class LibraryReader(Person):
    idn: int
    books: list

    def __init__(self, fio: str, books: list):
        self.fio = fio
        self.books = books

    def take_books(self, *args):
        for i in args:
            self.books.append(i)
        if len(args) < 4:
            print(f"{self.fio} взял книги: {', '.join(args)}")
        else:
            print(f"{self.fio} взял {len(args)} книги")

    def return_books(self, *args):
        for i in args:
            if i not in self.books:
                print(f"{self.fio} не брал {i}")
            else:
                self.books.remove(i)
                if len(args) < 4:
                    print(f"{self.fio} вернул книги: {', '.join(args)}")
                else:
                    print(f"{self.fio} вернул {len(args)} книги")


reader = LibraryReader("Тумилович Д.В.", ["книжка1", "книжка2"])
reader.take_books("book3", "book4")
reader.return_books("book3")
print(reader.books)
reader.return_books("book0")
