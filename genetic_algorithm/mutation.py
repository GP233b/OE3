import numpy as np
import sys
sys.path.append('../')
from config import X_MIN, X_MAX

# ====== Mutacje PyGAD zgodne z poprzednimi wersjami ======

def boundary_mutation(offspring, ga_instance):
    for i in range(offspring.shape[0]):
        if np.random.rand() < 0.5:
            idx = np.random.randint(offspring.shape[1])
            offspring[i][idx] = X_MIN if np.random.rand() < 0.5 else X_MAX
    return offspring

def single_point_mutation(offspring, ga_instance):
    for i in range(offspring.shape[0]):
        if np.random.rand() < 0.5:
            idx = np.random.randint(offspring.shape[1])
            offspring[i][idx] = np.random.uniform(X_MIN, X_MAX)
    return offspring

def two_point_mutation(offspring, ga_instance):
    for i in range(offspring.shape[0]):
        if np.random.rand() < 0.5:
            idx1, idx2 = np.random.choice(offspring.shape[1], 2, replace=False)
            offspring[i][idx1], offspring[i][idx2] = offspring[i][idx2], offspring[i][idx1]
    return offspring

def gaussian_mutation(offspring, ga_instance):
    for i in range(offspring.shape[0]):
        if np.random.rand() < 0.5:
            idx = np.random.randint(offspring.shape[1])
            offspring[i][idx] += np.random.normal(0, 20)
            offspring[i][idx] = np.clip(offspring[i][idx], X_MIN, X_MAX)
    return offspring
