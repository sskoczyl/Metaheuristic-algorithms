from xs_yang import XSYang
from pso import PSO


def main():
    in_data = input()
    vector = list(map(float, in_data.split()))
    time = vector[0]
    vector.pop(0)

    Searcher = PSO()
    Searcher.find_minima(XSYang(vector[5:]), vector[:5], max_time=time)

    for i in Searcher.best_argument():
        print(i, end=" ")

    print(Searcher.best_value())


if __name__ == '__main__':
    main()
