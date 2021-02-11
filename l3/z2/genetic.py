import random as rnd
import time
import pandas as pd
from subject import Subject


class Genetic:
    def __init__(self, path, vals, mset, cnt):
        self.dict = pd.read_table(path, header=None, names='w')
        self.best_sol = None
        self.best_val = None
        self.pop_count = cnt
        self.multiset = mset
        self.values = vals

    def best_value(self):
        return self.best_val

    def best_argument(self):
        return self.best_sol

    def find_maxima(self, start_sol, max_time):
        population = [Subject(i, self.evaluation(i)) for i in start_sol]

        t_end = time.time() + max_time
        while time.time() < t_end:
            strongest = self.select_strongest(population)

            for couple in strongest:

                new_genom = self.crossbreed(couple[0], couple[1])

                if new_genom in [p.genom for p in population]:
                    continue

                population.append(Subject(new_genom, self.evaluation(new_genom)) \
                                      if self.in_dict(new_genom) and self.can_assemble(new_genom) \
                                      else Subject(new_genom, 0))

            if len(population) > self.pop_count:
                population = sorted(population, key=lambda x: x.value, reverse=True)[0:self.pop_count]

        for e in population:
            print(e.genom)

        self.best_sol = sorted(population, key=lambda x: x.value, reverse=True)[0].genom
        self.best_val = self.evaluation(self.best_sol)

    def in_dict(self, word):
        return self.dict.isin([word]).any().any()

    def can_assemble(self, word):
        for x in word:
            if x not in self.multiset or len(word) > len(self.multiset):
                return False
            else:
                if word.count(x) > self.multiset.count(x):
                    return False

        return True

    def evaluation(self, word):
        val = 0

        for x in word:
            val += self.values[x]

        return val

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

    @staticmethod
    def select_strongest(population):
        k = int(len(population) * 0.6)
        best_individuals = sorted(population, key=lambda x: x.value, reverse=True)[0:k]

        return list(zip(best_individuals, best_individuals[::-1]))

    def crossbreed(self, a, b):
        ran_a, ran_b = rnd.randint(0, len(a.genom) - 1), rnd.randint(0, len(b.genom) - 1)

        if rnd.random() > 0.5:
            return self.random_mutation(a.genom[0:ran_a] + b.genom[ran_b:])
        else:
            return self.random_mutation(b.genom[0:ran_b] + a.genom[ran_a:])
