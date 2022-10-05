import pygame as pg
from .cell_view import CellView


class GridView:
    def __init__(self, grid_model, cell_size, color_theme):
        self.model = grid_model
        self.cell_size = cell_size
        self.cell_view = CellView(cell_size)  # FIXME: cell_size * 0.01 as secoind arg
        self.color_theme = color_theme

    def render(self, window: pg.surface):
        self.render_cells(window)
        self.render_pathfinding(window)

    def render_cells(self, window):
        for x, col in enumerate(self.model.grid):
            for y, cell in enumerate(col):
                self.cell_view.render(window, self.cell_size[0] * x, self.cell_size[1] * y, cell, self.color_theme.default)

    def render_pathfinding(self, window):
        for x, y in self.model.pathfinder.visited_order:
            self.cell_view.render(window, self.cell_size[0] * x, self.cell_size[1] * y, self.model.grid[x][y], self.color_theme.visited)

        if self.model.finished:
            current = self.model.cur_node

            while current is not None:
                self.cell_view.render(window, self.cell_size[0] * current.pos[0], self.cell_size[1] * current.pos[1], self.model.grid[current.pos[0]][current.pos[1]], self.color_theme.path)
                current = current.prev_node

        self.cell_view.render(window, self.cell_size[0] * self.model.start[0], self.cell_size[1] * self.model.start[1], self.model.grid[self.model.start[0]][self.model.start[1]], self.color_theme.start)
        self.cell_view.render(window, self.cell_size[0] * self.model.end[0], self.cell_size[1] * self.model.end[1], self.model.grid[self.model.end[0]][self.model.end[1]], self.color_theme.end)