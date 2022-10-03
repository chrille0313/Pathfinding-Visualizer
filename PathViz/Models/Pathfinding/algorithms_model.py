import heapq

from .path_node_model import PathNode
from queue import Queue, PriorityQueue
import heapq
from math import sqrt


class BFS:
    def __init__(self, world, start, end):
        self.world = world
        self.visited = set()
        self.visited_order = []

        self.q = Queue()
        self.q.put(PathNode(start))

        self.end = end

    def next(self):
        current_path_node: PathNode = self.q.get()

        self.visited_order.append(current_path_node.pos)

        if current_path_node.pos == self.end:
            return current_path_node, True

        for adj in self.world.get_adjacent(current_path_node.pos):
            if adj not in self.visited:
                self.visited.add(adj)
                self.q.put(PathNode(adj, current_path_node))

        return current_path_node, False


class Dijsktra:
    def __init__(self, world, start, end):
        self.world = world
        self.visited = set()
        self.visited_order = []

        self.q = []
        heapq.heappush(self.q, (0, PathNode(start)))

        self.end = end

    def next(self):
        cost, current_path_node = heapq.heappop(self.q)

        self.visited_order.append(current_path_node.pos)

        if current_path_node.pos == self.end:
            return current_path_node, True

        for adj in self.world.get_adjacent(current_path_node.pos):
            if adj not in self.visited:
                self.visited.add(adj)
                heapq.heappush(self.q, (cost + 1, PathNode(adj, current_path_node)))

        return current_path_node, False


class AStar:
    def __init__(self, world, start, end):
        self.world = world
        self.visited = set()
        self.visited_order = []

        self.q = []
        heapq.heappush(self.q, (0, PathNode(start)))

        self.end = end

    def dist(self, pos):
        return sqrt((pos[0] - self.end[0]) ** 2 + (pos[1] - self.end[1]) ** 2)

    def next(self):
        cost, current_path_node = heapq.heappop(self.q)

        self.visited_order.append(current_path_node.pos)

        if current_path_node.pos == self.end:
            return current_path_node, True

        for adj in self.world.get_adjacent(current_path_node.pos):
            if adj not in self.visited:
                self.visited.add(adj)
                heapq.heappush(self.q, (cost + self.dist(adj), PathNode(adj, current_path_node)))

        return current_path_node, False
