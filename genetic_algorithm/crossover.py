import numpy as np

def one_point_crossover(parents, offspring_size, ga_instance):
    offspring = np.empty(offspring_size)
    for k in range(offspring_size[0]):
        parent1 = parents[k % parents.shape[0]]
        parent2 = parents[(k + 1) % parents.shape[0]]
        point = np.random.randint(1, parents.shape[1])
        offspring[k, :point] = parent1[:point]
        offspring[k, point:] = parent2[point:]
    return offspring

def two_point_crossover(parents, offspring_size, ga_instance):
    offspring = np.empty(offspring_size)
    for k in range(offspring_size[0]):
        parent1 = parents[k % parents.shape[0]]
        parent2 = parents[(k + 1) % parents.shape[0]]
        pt1, pt2 = sorted(np.random.choice(range(1, parents.shape[1]), 2, replace=False))
        offspring[k, :pt1] = parent1[:pt1]
        offspring[k, pt1:pt2] = parent2[pt1:pt2]
        offspring[k, pt2:] = parent1[pt2:]
    return offspring

def uniform_crossover(parents, offspring_size, ga_instance):
    offspring = np.empty(offspring_size)
    for k in range(offspring_size[0]):
        parent1 = parents[k % parents.shape[0]]
        parent2 = parents[(k + 1) % parents.shape[0]]
        mask = np.random.randint(0, 2, parents.shape[1])
        offspring[k] = np.where(mask, parent1, parent2)
    return offspring

def granular_crossover(parents, offspring_size, ga_instance, grain_size=2):
    offspring = np.empty(offspring_size)
    for k in range(offspring_size[0]):
        parent1 = parents[k % parents.shape[0]].copy()
        parent2 = parents[(k + 1) % parents.shape[0]].copy()
        child = parent1.copy()
        for i in range(0, parents.shape[1], grain_size):
            if np.random.rand() < 0.5:
                child[i:i+grain_size] = parent2[i:i+grain_size]
        offspring[k] = child
    return offspring

