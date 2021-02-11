import random


class Particle:
    def __init__(self, x):
        self.current_pos = []
        self.velocity = []
        self.best_argument = []
        self.best_value = None
        self.current_val = None
        self.dimensions = len(x)

        for i in range(0, self.dimensions):
            self.velocity.append(random.uniform(-1, 1))
            self.current_pos.append(x[i])

    def evaluate(self, Function):
        self.current_val = Function(self.current_pos)

        if self.best_value is None or self.current_val < self.best_value:
            self.best_argument, self.best_value = self.current_pos, self.current_val

    def do_move(self):
        for i in range(0, self.dimensions):
            self.current_pos[i] = self.current_pos[i] + self.velocity[i]

    def accelerate(self, best_global):
        w, cognitive, social = 0.5, 1, 2

        for i in range(0, self.dimensions):
            vel_cognitive = cognitive * random.random() * (self.best_argument[i] - self.current_pos[i])
            vel_social = social * random.random() * (best_global[i] - self.current_pos[i])
            self.velocity[i] = w * self.velocity[i] + vel_cognitive + vel_social
