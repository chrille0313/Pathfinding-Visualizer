import heapq

from .path_node_model import PathNode
from queue import Queue, PriorityQueue
import heapq
from math import sqrt, inf


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
        self.distances = {(x, y): inf for x in range(world.size[0]) for y in range(world.size[1])}
        self.visited = set()
        self.visited_order = []

        self.q = []
        heapq.heappush(self.q, (0, PathNode(start)))

        self.end = end

    def next(self):
        current_cost, current_path_node = heapq.heappop(self.q)

        self.visited.add(current_path_node.pos)
        self.visited_order.append(current_path_node.pos)

        if current_path_node.pos == self.end:
            return current_path_node, True

        for adj in self.world.get_adjacent(current_path_node.pos):
            new_cost = current_cost + 1
            if adj not in self.visited and new_cost < self.distances[adj]:
                self.distances[adj] = new_cost
                heapq.heappush(self.q, (new_cost, PathNode(adj, current_path_node)))

        return current_path_node, False


class AStar:
    def __init__(self, world, start, end):
        self.world = world
        self.distances = {(x, y): inf for x in range(world.size[0]) for y in range(world.size[1])}
        self.visited = set()
        self.visited_order = []

        self.q = []
        heapq.heappush(self.q, (self.euclidean_dist(start, end), self.euclidean_dist(start, end), 0, PathNode(start)))
        self.distances[start] = 0

        self.start = start
        self.end = end

    def euclidean_dist(self, a, b):
        return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    def manhattan_dist(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def next(self):
        current_f_cost, current_h_cost, current_g_cost, current_path_node = heapq.heappop(self.q)

        self.visited.add(current_path_node.pos)
        self.visited_order.append(current_path_node.pos)

        if current_path_node.pos == self.end:
            return current_path_node, True

        for adj in self.world.get_adjacent(current_path_node.pos):
            new_g_cost = current_g_cost + self.manhattan_dist(current_path_node.pos, adj)
            new_h_cost = self.euclidean_dist(adj, self.end)
            new_f_cost = new_g_cost + new_h_cost

            if adj not in self.visited and new_g_cost < self.distances[adj]:
                self.distances[adj] = new_g_cost
                heapq.heappush(self.q, (new_f_cost, new_h_cost, new_g_cost, PathNode(adj, current_path_node)))

        return current_path_node, False
