import typing

import lib.entity


class Storage(typing.Protocol):
    def list(self) -> list[lib.entity.Book]: ...

    def put(self, books: typing.List[lib.entity.Book]) -> None: ...


class Books:
    def __init__(self, storage: Storage):
        self.storage = storage

    def create(self, book: lib.entity.Book) -> None:
        books = self.storage.list()
        books.append(book)
        self.storage.put(books)

    def delete(self, id: str) -> None:
        books = self.storage.list()
        books = list(filter(lambda book: book.id != id, books))
        self.storage.put(books)

    def change_status(self, id: str, status: lib.entity.Status) -> bool:
        books, changed = self.storage.list(), False

        for book in books:
            if book.id == id:
                book.status = status
                changed = True
                break

        if not changed:
            return False

        self.storage.put(books)
        return True

    def list(self) -> list[lib.entity.Book]:
        return self.storage.list()

    def search(self, field: str, value: str) -> typing.List[lib.entity.Book]:
        books = self.storage.list()

        match field:
            case "author":
                return list(filter(lambda book: book.author == value, books))
            case "title":
                return list(filter(lambda book: book.title == value, books))
            case "year":
                return list(filter(lambda book: book.year == int(value), books))
            case _:
                raise ValueError

        return books
