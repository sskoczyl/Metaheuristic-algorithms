import time
import random
import numpy as np


class SimulatedAnnealing(object):

    def __init__(self, fnc):
        self.Function = fnc
        self.best_solution = None
        self.best_value = None

    def get_best_solution(self):
        return self.best_solution

    def get_best_value(self):
        return self.Function(self.best_solution)

    def find_minima(self, max_time, start_solution):
        np.seterr(over='ignore')
        current_solution = self.best_solution = start_solution
        self.best_value = self.Function(self.best_solution)
        current_value = self.Function(self.best_solution)
        radius = 1
        temperature = 20
        epoch = 5
        t_end = time.time() + max_time

        while time.time() < t_end:
            for i in range(epoch):
                temp_solution = self.get_neighbor(current_solution, radius)
                temp_value = self.Function(temp_solution)

                if self.best_value > temp_value:
                    self.best_solution = temp_solution
                    self.best_value = temp_value

                delta = temp_value - current_value

                if 0 > delta:
                    current_solution = temp_solution
                    current_value = temp_value
                else:
                    x = random.random()

                    if x < np.exp((-delta) / temperature):
                        current_solution = temp_solution
                        current_value = temp_value

            temperature *= 0.9
            #radius *= 0.999

    def get_neighbor(self, vector, radius):
        norm = 0
        new_vector = []
        """"
        for i in range(len(vector)):
            new_vector.append(random.random())
            norm += (new_vector[i] - vector[i]) ** 2

        norm = np.sqrt(norm)

        for i in range(len(new_vector)):
            new_vector[i] *= radius
            new_vector[i] /= norm
        """
        r = random.random()

        for x in vector:
            new_vector.append(x + (r * radius))

        return new_vector
