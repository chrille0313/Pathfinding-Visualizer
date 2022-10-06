from enum import Enum, auto


class Cell(Enum):
    UNVISITED = auto()
    PATH = auto()
    WALL = auto()