import pygame as pg
from pygame import Vector2
from PathViz.Cell.View import CellView
from PathViz.Grid.Model import GridModel
from PathViz.colors import CellColorTheme


class GridView:
    def __init__(self, color_theme: CellColorTheme):
        self.viewed_model: GridModel | None = None
        self.cell_view = CellView()
        self.color_theme = color_theme

    def get_cell_size(self, display_size: Vector2):
        columns, rows = self.viewed_model.size
        return Vector2(display_size.x / columns, display_size.y / rows)

    def view_model(self, grid: GridModel, display_size: Vector2):
        if grid is not None:
            self.viewed_model = grid
            self.cell_view.set_size(self.get_cell_size(display_size))

    def render(self, window: pg.surface):
        self.render_cells(window)
        self.render_pathfinding(window)

    def render_cells(self, window):
        for y, row in enumerate(self.viewed_model.grid):
            for x, cell in enumerate(row):
                self.cell_view.render(window, self.cell_view.get_size().x * x, self.cell_view.get_size().y * y, cell, self.color_theme.default, self.color_theme.wall)

    def render_pathfinding(self, window):
        for x, y in self.viewed_model.pathfinder.visited_order:
            self.cell_view.render(window, self.cell_view.get_size().x * x, self.cell_view.get_size().y * y, self.viewed_model.grid[x][y], self.color_theme.visited, self.color_theme.wall)

        for x, y in self.viewed_model.pathfinder.searching:
            self.cell_view.render(window, self.cell_view.get_size().x * x, self.cell_view.get_size().y * y, self.viewed_model.grid[x][y], self.color_theme.searching, self.color_theme.wall)

        if self.viewed_model.finished:
            current = self.viewed_model.cur_node

            while current is not None:
                self.cell_view.render(window, self.cell_view.get_size().x * current.pos[0], self.cell_view.get_size().y * current.pos[1], self.viewed_model.grid[current.pos[0]][current.pos[1]], self.color_theme.path, self.color_theme.wall)
                current = current.prev_node

        self.cell_view.render(window, self.cell_view.get_size().x * self.viewed_model.start[0], self.cell_view.get_size().y * self.viewed_model.start[1], self.viewed_model.grid[self.viewed_model.start[0]][self.viewed_model.start[1]], self.color_theme.start, self.color_theme.wall)
        self.cell_view.render(window, self.cell_view.get_size().x * self.viewed_model.end[0], self.cell_view.get_size().y * self.viewed_model.end[1], self.viewed_model.grid[self.viewed_model.end[0]][self.viewed_model.end[1]], self.color_theme.end, self.color_theme.wall)