from enum import Enum, auto


class EventManager:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event, fn):
        if event not in self.subscribers:
            self.subscribers[event] = []

        self.subscribers[event].append(fn)

    def unsubscribe(self, event, fn):
        if event not in self.subscribers:
            return

        self.subscribers[event].remove(fn)

    def publish(self, event, *data):
        if event not in self.subscribers:
            return

        for fn in self.subscribers[event]:
            fn(*data)


class Event(Enum):
    MODEL_UPDATED = auto()
