import pygame as pg
from pygame import Vector2
from PathViz.events import EventManager, Event
from PathViz.Grid.Model import GridModel
from PathViz.Cell.Model import CellModel


class AppModel:
    def __init__(self, grid_size: Vector2, fps=60):
        self.running = False
        self.fps = fps
        self.event_manager = EventManager()

        rows, columns = grid_size
        self.grid = GridModel([[CellModel() for _ in range(int(columns))] for _ in range(int(rows))])

    def init(self):
        pg.init()
        self.running = True

    def quit(self):
        self.running = False

    def subscribe(self, event, fn):
        self.event_manager.subscribe(event, fn)

    def unsubscribe(self, event, fn):
        self.event_manager.unsubscribe(event, fn)

    def dispatch_app_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
                break

    def update(self):
        self.grid.update()
        self.event_manager.publish(Event.MODEL_UPDATED)

    def run(self):
        self.init()
        self.main_loop()
        self.quit()

    def main_loop(self):
        clock = pg.time.Clock()

        while self.running:
            self.dispatch_app_events()
            self.update()
            clock.tick(self.fps)
