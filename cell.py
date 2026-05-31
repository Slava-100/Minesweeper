from enum import Enum


class TypeCell(Enum):
    empty = (1,)
    number = (2,)
    bomb = 3


class Cell:
    def __init__(self):
        self.value = None
        self.type = None
        self.isOpen = False
