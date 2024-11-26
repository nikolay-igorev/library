import dataclasses
import enum


class Status(enum.StrEnum):
    exists = "exists"
    reserved = "reserved"


@dataclasses.dataclass
class Book:
    id: str
    title: str
    author: str
    year: int
    status: Status

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        return cls(**data)

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)

    def __str__(self) -> str:
        return f"ID: {self.id}. Title: {self.title}. Author: {self.author}. Status: {self.status}."
