class NewGuestPostCounterSingleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.counter = 0

    def get_counter(self):
        return self.counter

    def add_one(self):
        self.counter += 1

    def reset_counter(self):
        self.counter = 0
