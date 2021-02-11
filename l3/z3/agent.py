import numpy as np


class Agent:

    def __init__(self, arr):
        self.height = len(arr)
        self.length = len(arr[0])
        self.grid = arr
        self.agent_coords = np.array([np.where(self.grid == 5)[0][0], np.where(self.grid == 5)[1][0]])
        self.directions = {'U': np.array([-1, 0]), 'D': np.array([1, 0]), 'R': np.array([0, 1]), 'L': np.array([0, -1])}

    def evaluation(self, perm):
        coords = self.agent_coords
        for i in range(len(perm)):
            coords, value = np.add(coords, self.directions[perm[i]]), self.this_field(coords)
            if value is not None and value != 1:
                if self.this_field(coords) == 8:
                    return i + 1
            else:
                return -1

        return 0

    def this_field(self, coords):
        return self.grid[coords[0], coords[1]] if coords[0] < self.height and coords[1] < self.length else None if \
            coords[0] >= 0 and coords[1] >= 0 else None
