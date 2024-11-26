import typing
import uuid

import lib.entity


class Repository(typing.Protocol):
    def list(self) -> typing.List[lib.entity.Book]: ...

    def search(self, field: str, value: str) -> typing.List[lib.entity.Book]: ...

    def create(self, book: lib.entity.Book): ...

    def delete(self, id: str): ...


class ConsoleService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def handle_add(self):
        book_data = {"id": str(uuid.uuid4()), "status": lib.entity.Status.exists}

        book_data["title"] = input("Title: ")
        book_data["author"] = input("Author: ")
        book_data["year"] = int(input("Year: "))

        self.repository.create(lib.entity.Book.from_dict(book_data))

    def handle_delete(self):
        self.repository.delete(input("Book id: "))

    def handle_list(self):
        for book in self.repository.list():
            print(book)

    def handle_search(self):
        field = input("Which field to filter by (title, author or year)? ")
        value = input("Value: ")

        try:
            books = self.repository.search(field, value)
        except ValueError:
            print("Field or value is incorrect:  ", field, " / ", value)
            return

        for book in books:
            print(book)

    def handle_change_status(self):
        id = input("Book id: ")

        try:
            status = lib.entity.Status(input("Target status (exists / reserved): "))
        except ValueError:
            print("Incorrect status, only exists / reserved allowed.")
            return

        if self.repository.change_status(id, status):
            print("Success! Status has been changed.")
        else:
            print("Book not found.")
