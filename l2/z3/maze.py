import time
import random
import numpy as np


class SimulatedAnnealing(object):

    def __init__(self, a):
        self.Agent = a
        self.best_solution = None
        self.best_perm = None

    def get_best_solution(self):
        return self.best_solution

    def get_best_value(self):
        return len(self.best_solution)

    def find_minima(self, max_time):
        self.best_solution = self.Agent.get_start_solution()
        self.best_perm = self.Agent.evaluate_function(self.best_solution)
        current_sol = self.best_solution
        temp = 50
        epoch = 5
        t_end = time.time() + max_time

        while time.time() < t_end:
            for i in range(epoch):
                temp_sol = self.Agent.get_neighbour(current_sol)
                temp_perm = self.Agent.evaluate_function(temp_sol)
                current_perm = self.Agent.evaluate_function(current_sol)

                if temp_perm != -1 and current_perm != -1:
                    if temp_perm < len(self.best_solution):
                        self.best_solution = temp_sol
                        self.best_perm = temp_perm

                    delta = temp_perm - current_perm

                    if delta < 0:
                        current_sol = temp_sol
                    else:
                        x = random.random()
                        if x < np.exp((-delta) / temp):
                            current_sol = temp_sol

            temp *= 0.9
