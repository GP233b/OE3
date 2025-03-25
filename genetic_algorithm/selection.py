import numpy as np
def tournament_selection(pop, scores, k=3):
    selected = np.random.choice(len(pop), k, replace=False)
    return pop[min(selected, key=lambda i: scores[i])]