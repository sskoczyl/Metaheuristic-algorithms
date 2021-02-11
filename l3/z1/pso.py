from particle import Particle
import time


class PSO:
    def __init__(self):
        self.best_val = None
        self.best_sol = []
        self.swarm = []

    def best_value(self):
        return self.best_val

    def best_argument(self):
        return self.best_sol

    def create_swarm(self, start_x, cnt):
        self.swarm = []

        for i in range(0, cnt):
            self.swarm.append(Particle(start_x))

    def find_minima(self, Function, x, max_time=10, particle_cnt=20):
        self.create_swarm(x, particle_cnt)

        t_end = time.time() + max_time
        while time.time() < t_end:
            for j in range(0, len(self.swarm)):
                self.swarm[j].evaluate(Function)

                if self.best_val is None or self.swarm[j].current_val < self.best_val:
                    self.best_sol = list(self.swarm[j].current_pos)
                    self.best_val = float(self.swarm[j].current_val)

            for j in range(0, len(self.swarm)):
                self.swarm[j].accelerate(self.best_sol)
                self.swarm[j].do_move()
