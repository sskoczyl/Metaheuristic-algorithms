import random as rnd


class Path:

    def __init__(self, g, v):
        self.genom = g[:v]
        self.value = v
