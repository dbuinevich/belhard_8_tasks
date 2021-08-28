"""
Создать класс BookCard, в классе должны быть закрытые атрибуты:

- author - автор
- title - название книги
- publishing_house - издательство
- year - год издания
- num_pages - количество страниц
- num_copies - тираж

Определить методы:

- инициализатор __init__
- магические методы сравнения для сортировки книг по году издания

в сеттерах сделать проверки на тип данных. Если тип данных не подходит, то генерировать
ValueError. Для года издания дополнительно проверить на валидность, num_pages и
num_copies должны быть больше 0

реализовать через property
"""
import datetime


class BookCard:
    __author: str
    __title: str
    __publishing_house: str
    __year: int
    __num_pages: int
    __num_copies: int

    def __init__(self, author: str, title: str, publishing_house: str, year: str, num_pages: str, num_copies: str):
        self.__author = author
        self.__title = title
        self.__publishing_house = publishing_house
        self.__year = year
        self.__num_pages = num_pages
        self.__num_copies = num_copies

    def __eq__(self, other):
        return self.__year == other.__year

    def __ne__(self, other):
        return self.__year != other.__year

    def __lt__(self, other):
        return self.__year < other.__year

    def __le__(self, other):
        return self.__year <= other.__year

    def __gt__(self, other):
        return self.__year > other.__year

    def __ge__(self, other):
        return self.__year >= other.__year

    @property
    def author_1(self):
        return self.__author

    @author_1.setter
    def author_1(self, author: str):
        if isinstance(author, str) is False:
            raise ValueError("Enter correct author")
        else:
            self.__author = author

    @property
    def title_2(self):
        return self.__title

    @title_2.setter
    def title_2(self, title: str):
        if isinstance(title, str) is False:
            raise ValueError("Enter correct title")
        else:
            self.__title = title

    @property
    def publishing_house_3(self):
        return self.__publishing_house

    @publishing_house_3.setter
    def publishing_house_3(self, publishing_house: str):
        if isinstance(publishing_house, str) is False:
            raise ValueError("Enter correct publishing_house")
        else:
            self.__publishing_house = publishing_house

    @property
    def year_4(self):
        return self.__year

    @year_4.setter
    def year_4(self, year: int):
        now = datetime.datetime.now().year
        if isinstance(year, int) is False or year > now:
            raise ValueError("Enter correct year")
        else:
            self.__year = year

    @property
    def num_pages_5(self):
        return self.__num_pages

    @num_pages_5.setter
    def num_pages_5(self, num_pages: int):
        if isinstance(num_pages, int) is False or num_pages <= 0:
            raise ValueError("Enter correct num_pages")
        else:
            self.__num_pages = num_pages

    @property
    def num_copies_6(self):
        return self.__num_copies

    @num_copies_6.setter
    def num_copies_6(self, num_copies: int):
        if isinstance(num_copies, int) is False or num_copies <= 0:
            raise ValueError("Enter correct num_copies")
        else:
            self.__num_copies = num_copies


knizhka1 = BookCard("author1", "title1", "PH1", 1997, 25, 2)
# knizhka1.author_1 = 52
# knizhka1.author_1 = "authorX"
# print(knizhka1.author_1)
knizhka2 = BookCard("author2", "title2", "PH2", 1999, 30, 3)
# knizhka2.title_2 = 123
knizhka3 = BookCard("author3", "title3", "PH3", 2000, 30, 3)
# knizhka3.publishing_house_3 = 444
knizhka4 = BookCard("author4", "title4", "PH4", 2001, 10, 4)
# knizhka4.year_4 = 2022
knizhka5 = BookCard("author5", "title5", "PH5", 2003, 85, 8)
# knizhka5.num_pages_5 = ["kj", 123]
knizhka6 = BookCard("author6", "title6", "PH6", 2005, 88, 9)
# knizhka6.num_copies_6 = -4
books_list = [knizhka1, knizhka2, knizhka3, knizhka4, knizhka5, knizhka6]
books_list.sort()
print(books_list[0].year_4)
print(books_list[1].year_4)
print(books_list[2].year_4)
print(books_list[3].year_4)
print(books_list[4].year_4)
print(books_list[5].year_4)
