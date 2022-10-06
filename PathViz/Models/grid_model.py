from .cell_model import Cell
from .maze_model import PrimsMaze
from .Pathfinding import algorithms_model as Algorithms


class GridModel:
    def __init__(self, grid_size, algorithm=Algorithms.BFS):
        self.maze, self.start, self.end = PrimsMaze.create(*grid_size)
        self.size = grid_size
        self.pathfinder = algorithm(self, self.start, self.end)
        self.cur_node = None
        self.finished = False

    def update(self):
        if not self.finished:
            self.cur_node, self.finished = self.pathfinder.next()

    def is_valid_pos(self, row, col):
        return 0 <= row < self.size[0] and 0 <= col < self.size[1] and self.maze[row][col] == Cell.PATH

    def get_adjacent(self, node) -> list:
        adjacent = []
        node_row, node_col = node

        for row, col in ((node_row, node_col - 1),
                         (node_row + 1, node_col),
                         (node_row, node_col + 1),
                         (node_row - 1, node_col)):
            if self.is_valid_pos(row, col):
                adjacent.append((row, col))

        return adjacent
