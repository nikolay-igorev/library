import json
import typing

from lib.entity import Book


class JSONStorage:
    def __init__(self, fpath: str) -> None:
        self.fpath = fpath

    def list(self) -> list[Book]:
        with open(self.fpath) as fout:
            data = json.load(fout)
        return [Book.from_dict(book) for book in data]

    def put(self, books: typing.List[Book]) -> None:
        data = [book.to_dict() for book in books]
        with open(self.fpath, "w") as fin:
            json.dump(data, fin, indent=4)
