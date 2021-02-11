import time
import random as rnd
from path import Path


class Genetic:

    def __init__(self, a, p):
        self.Agent = a
        self.best_solution = None
        self.best_perm = None
        self.pop_count = p
        self.best_sol = None
        self.best_val = None

    def get_best_solution(self):
        return self.best_sol

    def get_best_value(self):
        return self.best_val

    def find_minima(self, start_sol, max_time):

        t_end = time.time() + max_time
        while time.time() < t_end:
            population = [Path(i, self.Agent.evaluation(i)) for i in start_sol]

            t_end = time.time() + max_time
            while time.time() < t_end:
                strongest = self.select_strongest(population)

                for couple in strongest:

                    new_genom = self.crossbreed(couple[0], couple[1])

                    if new_genom in [p.genom for p in population]:
                        continue
                    else:
                        population.append(Path(new_genom, self.Agent.evaluation(new_genom)))

                if len(population) > self.pop_count:
                    population = self.choose_subjects(population)[0:self.pop_count]

            self.best_sol = sorted(population, key=lambda x: x.value, reverse=True)[0].genom
            self.best_val = self.Agent.evaluation(self.best_sol)

    @staticmethod
    def random_mutation(genotype):
        if rnd.random() > 0.55:
            return genotype

        r = rnd.randint(0, 2)
        if r == 0:
            i = rnd.randint(0, len(genotype) - 1)
            genotype += genotype[i] if rnd.random() > 0.5 else genotype[i] + genotype
        elif r == 1:
            genotype = genotype.replace(genotype[rnd.randint(0, len(genotype) - 1)], "")
        elif r == 2:
            i, j = rnd.randint(0, len(genotype) - 1), rnd.randint(0, len(genotype) - 1)
            genotype = list(genotype)
            genotype[i], genotype[j] = genotype[j], genotype[i]
            genotype = "".join(genotype)

        return genotype

    def choose_subjects(self, pop):
        bad, neutral, ok = [], [], []

        for p in pop:
            if p.value == -1:
                bad.append(p)
            elif p.value == 0:
                neutral.append(p)
            else:
                ok.append(p)

        ok = sorted(ok, key=lambda x: x.value, reverse=False)

        return ok + neutral + bad

    @staticmethod
    def select_strongest(population):
        k = int(len(population) * 0.8)
        best_individuals = sorted(population, key=lambda x: x.value, reverse=True)[0:k]

        return list(zip(best_individuals, best_individuals[::-1]))

    def crossbreed(self, a, b):
        ran_a, ran_b = rnd.randint(0, len(a.genom) - 1), rnd.randint(0, len(b.genom) - 1)

        if rnd.random() > 0.5:
            return self.random_mutation(a.genom[0:ran_a] + b.genom[ran_b:])
        else:
            return self.random_mutation(b.genom[0:ran_b] + a.genom[ran_a:])
