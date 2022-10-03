from enum import Enum, auto


WIDTH = 30
HEIGHT = 30

WIN_WIDTH = 600
WIN_HEIGHT = 600


class Colors:
    BG = (50, 50, 50)
    GRID = (180, 180, 180)
    VISITED = 0x09CDDA
    PATH = (255, 255, 0)
    START_STOP = (0, 200, 0)


class Event(Enum):
    APP_UPDATE = auto()
