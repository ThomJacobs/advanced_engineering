import sqlite3
from enum import Enum
from dataclasses import dataclass
from abc import ABC, abstractmethod
class SQLiteType(Enum):
    NULL: str = 'NULL'
    INTEGER: str = 'INTEGER'
    REAL: str = 'REAL'
    TEXT: str = 'TEXT'


class SQLiteValue:
    def __init__(self, sql_type: SQLiteType) -> None:
        self._type: SQLiteType = sql_type

    @property
    def sql_type(self) -> SQLiteType:
        return self._type

    @abstractmethod
    def __eq__(self, other) -> None:
        pass


class SQLiteInteger(SQLiteValue):

    # Constructor:
    def __init__(self, value: int = 0) -> None:
        super().__init__(SQLiteType.INTEGER)

        # Instance attributes:
        self.value: int = value

    # Operators:
    def __eq__(self, other: int):
        self.value = other


class SQLiteText(SQLiteValue):

    # Constructor:
    def __init__(self, value: str = '') -> None:
        super().__init__(SQLiteType.TEXT)

        # Instance attributes:
        self.value: str = value


@dataclass
class User:

    # Instance attributes:
    identification: SQLiteInteger = SQLiteInteger()
    forename: SQLiteText() = SQLiteText()
    surname: SQLiteText() = SQLiteText()

    # Constructor:
    def __init__(self, identification: int, forename: str, surname: str):
        self.identification = SQLiteInteger(identification)
        self.forename = SQLiteText(forename)
        self.surname = SQLiteText(surname)

user: User = User(2, 'faye', 'jacobs')


print(user.surname.sql_type)
print(user.surname.value)