import numpy as np
import sys
sys.path.append('../')

from config import X_MIN, X_MAX
def gaussian_mutation(individual, rate):
    if np.random.rand() < rate:
        idx = np.random.randint(len(individual))
        individual[idx] += np.random.normal(0, 20)
        individual[idx] = np.clip(individual[idx], X_MIN, X_MAX)
    return individual