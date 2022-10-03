import pygame as pg


class CellView:
    def __init__(self, cell_size):
        self.cell = pg.Rect((0, 0), cell_size)

    def render(self, window, x, y, color):
        self.cell.topleft = (x, y)
        pg.draw.rect(window, color, self.cell)
