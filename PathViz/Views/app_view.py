import pygame as pg
from PathViz.globals import *
from .grid_view import GridView
from PathViz.events import Events


class AppView:
    def __init__(self, app_model, window_size):
        pg.init()
        self.window_size = window_size
        self.window = pg.display.set_mode(self.window_size)
        width, height = app_model.grid.size
        cell_size = window_size[0] / width, window_size[1] / height
        self.grid = GridView(app_model.grid, cell_size)

        Events.sub(Event.APP_UPDATE, self.render)

    def render(self):
        self.window.fill(Colors.BG)
        self.grid.render(self.window)
        pg.display.update()
