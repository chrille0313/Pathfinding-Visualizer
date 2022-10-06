import pygame as pg
from ..Models.cell_model import Cell


class CellView:
    def __init__(self, cell_size, wall_width=2):
        self.rect = pg.Rect((0, 0), cell_size)
        self.wall_width = wall_width

    def render(self, window, x, y, cell, colors):
        self.rect.topleft = x, y
        if cell == Cell.PATH:
            pg.draw.rect(window, colors.background, self.rect)
        else:
            pg.draw.rect(window, colors.wall, self.rect)

        pg.draw.circle(window, colors.wall, (x + self.rect.width // 2, y + self.rect.height // 2), 1)
