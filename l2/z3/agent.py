import numpy as np
import random


class Agent(object):

    def __init__(self, arr):
        self.height = len(arr)
        self.length = len(arr[0])
        self.grid = arr
        self.agent_coords = np.array([np.where(self.grid == 5)[0][0], np.where(self.grid == 5)[1][0]])
        self.directions = {'U': np.array([-1, 0]), 'D': np.array([1, 0]), 'R': np.array([0, 1]), 'L': np.array([0, -1])}
        self.prev_coords = None

    def get_start_solution(self):
        idx, path = 1, []
        position, forbidden = self.agent_coords, np.zeros((self.height, self.length))

        while self.this_field(position) != 8:

            move = self.check_if_forbidden(position, forbidden)

            if move is not None:
                position = np.add(position, self.directions[move])
                forbidden[position[0]][position[1]] = 1
                path.append(move)
                idx += 1
                self.prev_coords = move
            else:
                position = np.subtract(position, self.directions[path.pop()])

        return path

    def get_neighbour(self, solution):
        idx1, idx2 = random.randint(0, len(solution) - 1), random.randint(0, len(solution) - 1)
        while solution[idx1] == solution[idx2]:
            idx1, idx2 = random.randint(0, len(solution) - 1), random.randint(0, len(solution) - 1)

        new_solution = solution.copy()
        tmp = solution[idx1]
        new_solution[idx1], new_solution[idx2] = new_solution[idx2], tmp

        return new_solution

    def evaluate_function(self, perm):
        coords = self.agent_coords
        for i in range(len(perm)):
            coords, value = np.add(coords, self.directions[perm[i]]), self.this_field(coords)
            if value is not None and value != 1:
                if self.this_field(coords) == 8:
                    return i + 1
            else:
                return -1

    def this_field(self, coords):
        return self.grid[coords[0], coords[1]] if coords[0] < self.height and coords[1] < self.length else None if \
            coords[0] >= 0 and coords[1] >= 0 else None

    def not_occupied(self, current, visited):
        return False if self.this_field(current) == 1 or visited[current[0]][current[1]] == 1 else True

    def check_if_forbidden(self, position, visited):
        possible_moves = []

        if self.this_field(np.add(position, np.array([0, -1]))) is not None and self.not_occupied(
                np.add(position, np.array([0, -1])), visited):

            if self.this_field(np.add(position, np.array([0, -1]))) == 8:
                return 'L'

            possible_moves.append('L')

        if self.this_field(np.add(position, np.array([1, 0]))) is not None and self.not_occupied(
                np.add(position, np.array([0, 1])), visited):

            if self.this_field(np.add(position, np.array([1, 0]))) == 8:
                return 'R'

            possible_moves.append('R')

        if self.this_field(np.add(position, np.array([1, 0]))) is not None and self.not_occupied(
                np.add(position, np.array([1, 0])), visited):

            if self.this_field(np.add(position, np.array([1, 0]))) == 8:
                return 'D'

            possible_moves.append('D')

        if self.this_field(np.add(position, np.array([-1, 0]))) is not None and self.not_occupied(
                np.add(position, np.array([-1, 0])), visited):

            if self.this_field(np.add(position, np.array([-1, 0]))) == 8:
                return 'U'

            possible_moves.append('U')

        if len(possible_moves) == 0:
            return None
        if self.prev_coords in possible_moves:
            return self.prev_coords
        else:
            return possible_moves[random.randint(0, len(possible_moves) - 1)]
