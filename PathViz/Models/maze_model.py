class KruskalMaze:
    N, S, E, W = 1, 2, 4, 8
    DX = {E: 1, W: -1, N: 0, S: 0}
    DY = {E: 0, W: 0, N: -1, S: 1}
    OPPOSITE = {E: W, W: E, N: S, S: N}

    def __init__(self, width, height):
        self.maze, self.sets = self.init_maze_and_sets(width, height)
        self.edges = self.init_edges(width, height)

    @staticmethod
    def init_maze_and_sets(width, height):
        maze = [
            [0 for _ in range(width)] for _ in range(height)
        ]
        sets = [
            [Tree() for _ in range(width)] for _ in range(height)
        ]
        return maze, sets

    @staticmethod
    def init_edges(width, height):
        edges = []
        for y in range(height):
            for x in range(width):
                if y > 0:
                    edges.append((x, y, KruskalMaze.N))
                if x > 0:
                    edges.append((x, y, KruskalMaze.W))
        shuffle(edges)
        return edges

    def next(self):
        while self.edges:
            x, y, direction = self.edges.pop()
            nx, ny = x + KruskalMaze.DX[direction], y + KruskalMaze.DY[direction]
            set1, set2 = self.sets[y][x], sets[ny][nx]
            if not set1.is_connected(set2):
                set1.connect(set2)
                self.maze[y][x] |= direction
                self.maze[ny][nx] |= KruskalMaze.OPPOSITE[direction]
                return

    @staticmethod
    def display_maze(grid):
        print(" " + "_" * (len(grid[0]) * 3 - 1))
        for y, row in enumerate(grid):
            print("|", end="")
            for x, cell in enumerate(row):
                print("  " if (cell & KruskalMaze.S != 0) else "__", end="")
                if cell & KruskalMaze.E != 0:
                    print(" " if ((cell | row[x+1]) & KruskalMaze.S != 0) else "_", end="")
                else:
                    print("|", end="")
            print("")


class Tree:
    def __init__(self):
        self.parent = None

    @property
    def root(self):
        return self.parent.root if self.parent else self

    def is_connected(self, other):
        return self.root == other.root

    def connect(self, other):
        other.root.parent = self


maze = KruskalMaze(10, 10)
while True:
    maze.next()
    maze.display_maze(maze.maze)
    input()
