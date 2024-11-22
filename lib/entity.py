import dataclasses
import enum
import uuid

class Status(str, enum.Enum):
    exists = 'exists'
    reserved = 'reserved'

@dataclasses.dataclass
class Book:
    id: uuid.UUID
    title: str
    author: str
    year: int
    status: Status

    @classmethod
    def from_dict(cls, data: dict) -> 'Book':
        return cls(**data)

    @classmethod
    def to_dict(self) -> dict:
        return dataclasses.asdict(self)
