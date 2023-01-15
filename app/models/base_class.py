from re import compile
from typing import Any

from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Column = Column(Integer, primary_key=True, index=True)

    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        p = compile("[A-Z]{1}[a-z]*")
        name_apart = p.findall(cls.__name__)
        return "_".join(name_apart).lower()

    # todo
    # mixin : created_at, updated_at, deleted_at is_deleted
