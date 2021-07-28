class Singleton(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class NewGuestPostCounter(metaclass=Singleton):
    def __init__(self):
        self.counter = 0

    def get_counter(self):
        return self.counter

    def add_one(self):
        self.counter += 1

    def reset_counter(self):
        self.counter = 0
