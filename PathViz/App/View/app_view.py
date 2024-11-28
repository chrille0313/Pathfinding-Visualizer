import pygame as pg
from pygame import Vector2
from PathViz.App.Model import AppModel
from PathViz.Grid.View import GridView
from PathViz.events import Event
from PathViz.globals import Colors, COLOR_THEME


class AppView:
    def __init__(self, window_size: Vector2):
        pg.init()

        self.viewed_model: AppModel = None

        self.window_size = window_size
        self.window = pg.display.set_mode(self.window_size)

        self.grid_view = GridView(COLOR_THEME)

    def get_cell_size(self):
        rows, columns = self.viewed_model.grid.size
        return Vector2(self.window_size.x / columns, self.window_size.y / rows)

    def view_model(self, app: AppModel):
        if self.viewed_model is not None:
            self.viewed_model.unsubscribe(Event.MODEL_UPDATED, self.render)

        self.viewed_model = app
        self.grid_view.view_model(app.grid, self.get_cell_size())

        app.subscribe(Event.MODEL_UPDATED, self.render)

    def render(self):
        self.window.fill(Colors.BG)
        self.grid_view.render(self.window)
        pg.display.update()
