import pygame as pg
from pygame import Vector2
from PathViz.App.Model import AppModel
from PathViz.Grid.View import GridView
from PathViz.events import Event
from PathViz.colors import ColorTheme


class AppView:
    def __init__(self, window_size: Vector2, color_theme: ColorTheme):
        pg.init()

        self.viewed_model: AppModel | None = None

        self.window_size = window_size
        self.window = pg.display.set_mode(self.window_size)
        self.color_theme = color_theme

        self.grid_view = GridView(color_theme.cells)

    def view_model(self, app: AppModel):
        if self.viewed_model is not None:
            self.viewed_model.unsubscribe(Event.MODEL_UPDATED, self.render)

        if app is not None:
            self.viewed_model = app
            self.grid_view.view_model(app.grid, self.window_size)

            app.subscribe(Event.MODEL_UPDATED, self.render)

    def render(self):
        self.window.fill(self.color_theme.cells.default)
        self.grid_view.render(self.window)
        pg.display.update()
