from random import randint, shuffle
from cell_model import Cell


class PrimsMaze:
    @classmethod
    def create(cls, rows, cols):
        maze, walls = cls.init_maze(rows, cols)
        cls.prims_create(maze, walls)
        cls.make_unvisited_to_walls(maze, rows, cols)
        start, end = cls.create_entrance_exit(maze, rows, cols)
        return maze, start, end

    @staticmethod
    def init_maze(rows, cols):
        maze = [
            [Cell.UNVISITED for _ in range(cols)] for _ in range(rows)
        ]

        starting_row = randint(1, rows - 2)
        starting_col = randint(1, cols - 2)

        maze[starting_row][starting_col] = Cell.PATH
        walls = [(starting_row - 1, starting_col), (starting_row, starting_col - 1),
                 (starting_row, starting_col + 1), (starting_row + 1, starting_col)]

        maze[starting_row - 1][starting_col] = Cell.WALL
        maze[starting_row][starting_col - 1] = Cell.WALL
        maze[starting_row][starting_col + 1] = Cell.WALL
        maze[starting_row + 1][starting_col] = Cell.WALL

        return maze, walls

    @classmethod
    def prims_create(cls, maze, walls):
        while walls:
            cls.next(maze, walls)

    @classmethod
    def next(cls, maze, walls):
        while walls:
            row, col = walls[randint(0, len(walls) - 1)]
            if (col != 0 and maze[row][col - 1] == Cell.UNVISITED and maze[row][col + 1] == Cell.PATH) \
                    or (row != 0 and maze[row - 1][col] == Cell.UNVISITED and maze[row + 1][col] == Cell.PATH) \
                    or (row != len(maze) - 1 and maze[row + 1][col] == Cell.UNVISITED and maze[row - 1][col] == Cell.PATH) \
                    or (
                    col != len(maze[0]) - 1 and maze[row][col + 1] == Cell.UNVISITED and maze[row][col - 1] == Cell.PATH):
                cls.temp(maze, walls, row, col)
                return
            cls.delete_wall(walls, row, col)

    @staticmethod
    def make_unvisited_to_walls(maze, rows, cols):
        for row in range(rows):
            for col in range(cols):
                if maze[row][col] == Cell.UNVISITED:
                    maze[row][col] = Cell.WALL

    @staticmethod
    def create_entrance_exit(maze, rows, cols):
        start = end = 0
        for start in range(1, cols - 1):
            if maze[1][start] == Cell.PATH:
                maze[0][start] = Cell.PATH
                break
        for end in range(cols - 1, 0, -1):
            if maze[rows - 2][end] == Cell.PATH:
                maze[rows - 1][end] = Cell.PATH
                break
        return (0, start), (rows - 1, end)

    @staticmethod
    def delete_wall(walls, row, col):
        if (row, col) in walls:
            walls.remove((row, col))

    @staticmethod
    def surrounding_cells(maze, row, col):
        count = 0
        if maze[row - 1][col] == Cell.PATH:
            count += 1
        if maze[row + 1][col] == Cell.PATH:
            count += 1
        if maze[row][col - 1] == Cell.PATH:
            count += 1
        if maze[row][col + 1] == Cell.PATH:
            count += 1
        return count

    @classmethod
    def temp(cls, maze, walls, row, col):
        s_cells = cls.surrounding_cells(maze, row, col)
        if s_cells < 2:
            maze[row][col] = Cell.PATH
            if row != 0:
                if maze[row - 1][col] != Cell.PATH:
                    maze[row - 1][col] = Cell.WALL
                if [row - 1, col] not in walls:
                    walls.append((row - 1, col))
            if col != 0:
                if maze[row][col - 1] != Cell.PATH:
                    maze[row][col - 1] = Cell.WALL
                if [row, col - 1] not in walls:
                    walls.append((row, col - 1))
            if row != len(maze) - 1:
                if maze[row + 1][col] != Cell.PATH:
                    maze[row + 1][col] = Cell.WALL
                if [row + 1, col] not in walls:
                    walls.append((row + 1, col))
            if col != len(maze[0]):
                if maze[row][col + 1] != Cell.PATH:
                    maze[row][col + 1] = Cell.WALL
                if [row, col + 1] not in walls:
                    walls.append((row, col + 1))
        cls.delete_wall(walls, row, col)

    @staticmethod
    def print_maze(maze):
        for row in maze:
            for cell in row:
                print('# ' if cell == Cell.WALL else "  ", end="")
            print('')
