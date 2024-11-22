import typing
import uuid

from lib.entity import Book, Status
from lib.storage.json import JSONStorage


class Storage(typing.Protocol):
    def list(self) -> list[Book]:
        ...

    def put(self, books: typing.List[Book]) -> None:
        ...


class Books:

    def __init__(self):
        self.storage = JSONStorage()

    def create(self, book: Book) -> None:
        books = self.storage.list()
        books.append(book)
        self.storage.put(books)

    def delete(self, id: uuid.UUID) -> bool:
        books = self.storage.list()
        books = filter(lambda book: book.id != id, books)
        self.storage.put(list(books))

    def change_status(self, id: uuid.UUID, status: Status) -> Book | None:
        books = self.storage.list()
        book = filter(lambda book: book.id == id, books)
        if book:
            book.status = status
        else:
            print('The book does not exist.')

    def search(self, field: str, value: str | int) -> list[Book]:
        books = self.storage.list()
        if field == 'author':
            books = filter(lambda book: book.author == value, books)
        if field == 'title':
            books = filter(lambda book: book.title == value, books)
        if field == 'year':
            books = filter(lambda book: book.year == value, books)
        return list(books)
