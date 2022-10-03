from .Pathfinding.algorithms_model import *


class GridModel:
    def __init__(self, size):
        self.size = size
        self.visited = []
        self.start = (2, 2)
        self.end = (2, 27)
        self.pathfinder = AStar(self, self.start, self.end)
        self.finished = False
        self.cur_node = None

    def update(self):
        if not self.finished:
            self.cur_node, self.finished = self.pathfinder.next()

    def is_inside(self, x, y):
        return 0 <= x < self.size[0] and 0 <= y < self.size[1]

    def get_adjacent(self, node) -> list:
        adjacent = []
        node_x, node_y = node

        for x, y in ((node_x, node_y - 1), (node_x + 1, node_y), (node_x, node_y + 1), (node_x - 1, node_y)):
            if self.is_inside(x, y):
                adjacent.append((x, y))

        return adjacent
