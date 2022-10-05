import random
from .cell_model import CellModel
from .Pathfinding import algorithms_model as Algorithms


class GridModel:
    def __init__(self, grid=None, start=None, end=None, algorithm=Algorithms.AStar):
        self.grid = grid if grid is not None else [[CellModel()]]
        self.size = len(self.grid[0]), len(self.grid)
        self.start = start if start is not None else random.randint(0, self.size[0] - 1), random.randint(0, self.size[1] - 1)
        self.end = end if end is not None else random.randint(0, self.size[0] - 1), random.randint(0, self.size[1] - 1)
        self.pathfinder = algorithm(self, self.start, self.end)
        self.cur_node = None
        self.finished = False

    def update(self):
        if not self.finished:
            self.cur_node, self.finished = self.pathfinder.next()

    def is_inside(self, x, y):
        return 0 <= x < self.size[0] and 0 <= y < self.size[1]

    def get_adjacent(self, node) -> list:
        adjacent = []
        node_x, node_y = node

        for x, y in ((node_x, node_y - 1),
                     (node_x + 1, node_y - 1),
                     (node_x + 1, node_y),
                     (node_x + 1, node_y + 1),
                     (node_x, node_y + 1),
                     (node_x - 1, node_y + 1),
                     (node_x - 1, node_y),
                     (node_x - 1, node_y - 1)):
            if self.is_inside(x, y):
                adjacent.append((x, y))

        return adjacent
