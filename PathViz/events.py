class Events:
    subscribers = {}

    @classmethod
    def sub(cls, event, fn):
        if event not in cls.subscribers:
            cls.subscribers[event] = []

        cls.subscribers[event].append(fn)

    @classmethod
    def post(cls, event, *data):
        if event not in cls.subscribers:
            return

        for fn in cls.subscribers[event]:
            fn(*data)
