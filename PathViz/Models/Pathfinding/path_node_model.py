class PathNode:
    def __init__(self, current_node, prev_node=None, steps=0):
        self.pos = current_node
        self.prev_node = prev_node
        self.steps = steps

    def __lt__(self, other):
        return 0
