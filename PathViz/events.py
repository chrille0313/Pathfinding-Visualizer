from enum import Enum, auto

class Event(Enum):
    MODEL_UPDATED = auto()


class EventManager:
    def __init__(self):
        self.subscribers: dict[Event, callable] = {}

    def subscribe(self, event: Event, fn: callable):
        if event not in self.subscribers:
            self.subscribers[event] = []

        self.subscribers[event].append(fn)

    def unsubscribe(self, event: Event, fn: callable):
        if event not in self.subscribers:
            return

        self.subscribers[event].remove(fn)

    def unsubscribe_all(self, event: Event):
        if event not in self.subscribers:
            return

        self.subscribers[event] = []

    def clear_subscribers(self):
        self.subscribers = {}

    def publish(self, event: Event, *data):
        if event not in self.subscribers:
            return

        for fn in self.subscribers[event]:
            fn(*data)
