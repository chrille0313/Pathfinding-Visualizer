import pygame as pg
from pygame import Vector2
from PathViz.Cell.View import CellView
from PathViz.Grid.Model import GridModel


class GridView:
    def __init__(self, color_theme):
        self.viewed_model: GridModel = None
        self.cell_view = CellView()
        self.color_theme = color_theme

    def view_model(self, grid: GridModel, cell_size: Vector2):
        self.viewed_model = grid
        self.cell_view.set_size(cell_size)

    def render(self, window: pg.surface):
        self.render_cells(window)
        self.render_pathfinding(window)

    def render_cells(self, window):
        for x, col in enumerate(self.viewed_model.grid):
            for y, cell in enumerate(col):
                self.cell_view.render(window, self.cell_view.get_size().x * x, self.cell_view.get_size().y * y, cell, self.color_theme.default)

    def render_pathfinding(self, window):
        for x, y in self.viewed_model.pathfinder.visited_order:
            self.cell_view.render(window, self.cell_view.get_size().x * x, self.cell_view.get_size().y * y, self.viewed_model.grid[x][y], self.color_theme.visited)

        for x, y in self.viewed_model.pathfinder.searching:
            self.cell_view.render(window, self.cell_view.get_size().x * x, self.cell_view.get_size().y * y, self.viewed_model.grid[x][y], self.color_theme.searching)

        if self.viewed_model.finished:
            current = self.viewed_model.cur_node

            while current is not None:
                self.cell_view.render(window, self.cell_view.get_size().x * current.pos[0], self.cell_view.get_size().y * current.pos[1], self.viewed_model.grid[current.pos[0]][current.pos[1]], self.color_theme.path)
                current = current.prev_node

        self.cell_view.render(window, self.cell_view.get_size().x * self.viewed_model.start[0], self.cell_view.get_size().y * self.viewed_model.start[1], self.viewed_model.grid[self.viewed_model.start[0]][self.viewed_model.start[1]], self.color_theme.start)
        self.cell_view.render(window, self.cell_view.get_size().x * self.viewed_model.end[0], self.cell_view.get_size().y * self.viewed_model.end[1], self.viewed_model.grid[self.viewed_model.end[0]][self.viewed_model.end[1]], self.color_theme.end)