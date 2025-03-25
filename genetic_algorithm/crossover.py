import numpy as np
def one_point_crossover(parent1, parent2):
    point = np.random.randint(1, len(parent1))
    return np.concatenate((parent1[:point], parent2[point:])), np.concatenate((parent2[:point], parent1[point:]))