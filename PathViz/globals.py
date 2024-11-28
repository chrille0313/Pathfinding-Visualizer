from pygame import Vector2

class Colors:
    BG = (50, 50, 50)
    GRID = BG
    WALL = (0, 0, 0)
    VISITED = (194, 15, 0)
    SEARCHING = (105, 193, 0)  # (204, 204, 0)
    # PATH = (105, 193, 0)
    START = END = PATH = (37, 139, 174)


class CellColors:
    def __init__(self, background_color, wall_color):
        self.wall = wall_color
        self.background = background_color


class GridColorTheme:
    def __init__(self, default, start, end, path, visited, searching, wall):
        self.default = CellColors(default, wall)
        self.visited = CellColors(visited, wall)
        self.searching = CellColors(searching, wall)
        self.path = CellColors(path, wall)
        self.start = CellColors(start, wall)
        self.end = CellColors(end, wall)


GRID_SIZE = Vector2(30, 30)
WIN_SIZE = Vector2(600, 600)
COLOR_THEME = GridColorTheme(Colors.GRID, Colors.START, Colors.END, Colors.PATH, Colors.VISITED, Colors.SEARCHING, Colors.WALL)
