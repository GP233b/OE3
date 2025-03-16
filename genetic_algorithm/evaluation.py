import numpy as np
def schwefel(x):
    return 418.9829 * len(x) - sum(xi * np.sin(np.sqrt(abs(xi))) for xi in x)