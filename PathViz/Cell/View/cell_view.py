import pygame as pg
from pygame import Vector2

class CellView:
    def __init__(self, size=Vector2(0, 0), wall_width=2):  # FIXME: cell_size * 0.01 as wall_width (use dynamic wall width)
        self.rect = pg.Rect((0, 0), size)
        self.wall_width = wall_width

    def get_size(self):
        return Vector2(self.rect.size)

    def set_size(self, cell_size):
        self.rect.size = cell_size

    def render(self, window: pg.surface, x, y, cell, colors):
        self.rect.topleft = x, y
        pg.draw.rect(window, colors.background, self.rect)
        pg.draw.circle(window, colors.wall, (x + self.rect.width // 2, y + self.rect.height // 2), 1)

        # Because pygame is retarded in how it renders lines, I had to do it like this
        if cell.walls[0]:
            pg.draw.line(window, colors.wall, self.rect.topleft, (x + self.rect.width, y), self.wall_width)
        if cell.walls[1]:
            pg.draw.line(window, colors.wall, (x + self.rect.width - self.wall_width, y), (x + self.rect.width - self.wall_width, y + self.rect.height), self.wall_width)
        if cell.walls[2]:
            pg.draw.line(window, colors.wall, (x, y + self.rect.height - self.wall_width), (x + self.rect.width - self.wall_width // 2, y + self.rect.height - self.wall_width), self.wall_width)
        if cell.walls[3]:
            pg.draw.line(window, colors.wall, self.rect.bottomleft, self.rect.topleft, self.wall_width)
