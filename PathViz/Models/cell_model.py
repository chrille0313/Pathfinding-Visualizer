from enum import Enum, auto


class Cell(Enum):
    UNVISITED = auto()
    PATH = auto()
    WALL = auto()


class Cell2:
    def __init__(self, walls, weight, cell_type):
        self.walls = walls
        self.weight = weight
        self.cell_type = cell_type
