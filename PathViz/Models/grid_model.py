from .cell_model import Cell
from .maze_model import PrimsMaze
from .Pathfinding import algorithms_model as Algorithms


class GridModel:
    def __init__(self, grid_size, algorithm=Algorithms.AStar):
        self.maze, self.walls = PrimsMaze.init_maze(*grid_size)
        self.size = self.rows, self.cols = grid_size
        self.start = None
        self.end = None
        self.pathfinder = algorithm
        self.cur_node = None
        self.maze_finished = False
        self.pathfinding_finished = False

    def update(self):
        if not self.maze_finished:
            PrimsMaze.next(self.maze, self.walls)

            if not self.walls:
                PrimsMaze.make_unvisited_to_walls(self.maze, self.rows, self.cols)
                self.start, self.end = PrimsMaze.create_entrance_exit(self.maze, self.rows, self.cols)
                self.maze_finished = True
                self.pathfinder = self.pathfinder(self, self.start, self.end)

        elif not self.pathfinding_finished:
            self.cur_node, self.pathfinding_finished = self.pathfinder.next()

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
