# algorithm.py
import numpy as np
import sys
sys.path.append('../')
from config import *
from crossover import *
from evaluation import *
from selection import * 
from mutation import * 


def genetic_algorithm():
    pop = np.random.uniform(X_MIN, X_MAX, (POP_SIZE, DIM))
    for _ in range(GENS):
        scores = np.array([schwefel(ind) for ind in pop])
        new_pop = []
        for _ in range(POP_SIZE // 2):
            p1, p2 = tournament_selection(pop, scores), tournament_selection(pop, scores)
            c1, c2 = one_point_crossover(p1, p2) if np.random.rand() < CROSS_RATE else (p1, p2)
            new_pop.extend([gaussian_mutation(c1, MUT_RATE), gaussian_mutation(c2, MUT_RATE)])
        pop = np.array(new_pop)
    return pop[np.argmin([schwefel(ind) for ind in pop])]