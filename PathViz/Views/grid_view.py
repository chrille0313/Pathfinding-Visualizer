import pygame as pg
from .cell_view import CellView
from ..globals import *


class GridView:
    def __init__(self, grid_model, cell_size):
        self.model = grid_model
        self.cell_size = cell_size
        self.cell_view = CellView(cell_size)

    def render(self, window: pg.surface):
        self.render_grid(window)
        self.render_cells(window)

    def render_grid(self, window):
        width, height = self.model.size
        cell = pg.Rect((0, 0), self.cell_size)

        for x in range(width):
            for y in range(height):
                cell.topleft = (self.cell_size[0] * x, self.cell_size[1] * y)
                pg.draw.rect(window, Colors.GRID, cell, 1)

    def render_cells(self, window):
        for x, y in self.model.pathfinder.visited_order:
            self.cell_view.render(window, self.cell_size[0] * x, self.cell_size[1] * y, Colors.VISITED)

        if self.model.finished:
            current = self.model.cur_node

            while current is not None:
                self.cell_view.render(window, self.cell_size[0] * current.pos[0], self.cell_size[1] * current.pos[1], Colors.PATH)
                current = current.prev_node

        self.cell_view.render(window, self.cell_size[0] * self.model.start[0], self.cell_size[1] * self.model.start[1], Colors.START)
        self.cell_view.render(window, self.cell_size[0] * self.model.end[0], self.cell_size[1] * self.model.end[1], Colors.STOP)