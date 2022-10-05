from enum import Enum, auto


class Colors:
    BG = (50, 50, 50)
    GRID = BG
    WALL = (0, 0, 0)
    VISITED = 0x09CDDA
    PATH = (255, 255, 0)
    START = END = (0, 200, 0)


class Event(Enum):
    APP_UPDATE = auto()


class CellColors:
    def __init__(self, background_color, wall_color):
        self.wall = wall_color
        self.background = background_color


class GridColorTheme:
    def __init__(self, default, start, end, path, visited, wall):
        self.default = CellColors(default, wall)
        self.visited = CellColors(visited, wall)
        self.path = CellColors(path, wall)
        self.start = CellColors(start, wall)
        self.end = CellColors(end, wall)


WIDTH, HEIGHT = 30, 30
WIN_WIDTH, WIN_HEIGHT = 600, 600
COLOR_THEME = GridColorTheme(Colors.GRID, Colors.START, Colors.END, Colors.PATH, Colors.VISITED, Colors.WALL)
