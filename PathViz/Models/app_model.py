import pygame as pg
from .grid_model import GridModel
from PathViz.events import Events
from ..globals import Event


class AppModel:
    def __init__(self, grid_size):
        self.running = False
        self.grid_size = grid_size
        self.grid = GridModel(grid_size)

    def init(self):
        pg.init()
        self.running = True

    def quit(self):
        self.running = False

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
                break

    def update(self):
        self.grid.update()
        Events.post(Event.APP_UPDATE)
        pass

    def run(self):
        self.init()

        self.main_loop()

        self.quit()

    def main_loop(self):
        clock = pg.time.Clock()
        while self.running:
            self.events()
            self.update()
            clock.tick(0)
