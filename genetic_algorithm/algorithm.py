import sys

import numpy as np
from config import *
from genetic_algorithm.crossover import one_point_crossover
from genetic_algorithm.evaluation import schwefel
from genetic_algorithm.mutation import gaussian_mutation
from genetic_algorithm.selection import tournament_selection
from genetic_algorithm.visualization import plot_results


def genetic_algorithm():
    pop = np.random.uniform(X_MIN, X_MAX, (POP_SIZE, DIM))
    history = []
    for _ in range(GENS):
        scores = np.array([schwefel(ind) for ind in pop])
        best_score = np.min(scores)
        history.append(best_score)
        new_pop = []
        for _ in range(POP_SIZE // 2):
            p1, p2 = tournament_selection(pop, scores), tournament_selection(pop, scores)
            c1, c2 = one_point_crossover(p1, p2) if np.random.rand() < CROSS_RATE else (p1, p2)
            new_pop.extend([gaussian_mutation(c1, MUT_RATE), gaussian_mutation(c2, MUT_RATE)])
        pop = np.array(new_pop)
    plot_results(history)  # Zapisz wykres
    return pop[np.argmin([schwefel(ind) for ind in pop])]
