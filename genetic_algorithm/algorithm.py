import numpy as np
import time
from config import *
from genetic_algorithm.evaluation import schwefel
from genetic_algorithm.mutation import *
from genetic_algorithm.crossover import *
from genetic_algorithm.selection import *
from genetic_algorithm.save_iteration_graph import save_iteration_graph
from genetic_algorithm.visualization import plot_3d_result, plot_heatmap, plot_results

# Pseudo-argument 'ga_instance' wymagany przez pygad-style mutacje i krzyżowania
class DummyGA:
    def __init__(self):
        pass

# Zaktualizowana funkcja
def genetic_algorithm(mutation_function, crossover_function, selection_function, mutation_rate,
                      elitism_rate=1, pop_size=POP_SIZE, gens=GENS,
                      x_min=X_MIN, x_max=X_MAX, dim=DIM):

    start_time = time.time()
    
    mutation_func = globals()[mutation_function]
    crossover_func = globals()[crossover_function]
    selection_func = globals()[selection_function]
    ga_instance = DummyGA()  # Pseudo instancja GA

    pop = np.random.uniform(x_min, x_max, (pop_size, dim))
    history = []

    for iteration in range(gens):
        scores = np.array([schwefel(ind) for ind in pop])
        best_idx = np.argmin(scores)
        best_individual = pop[best_idx]
        best_score = scores[best_idx]
        history.append(best_score)

        if iteration % 50 == 1:
            save_iteration_graph(history, best_individual, iteration)

        # Elitaryzm
        new_pop = [best_individual] * elitism_rate

        # Selekcja par
        num_offspring = pop_size - elitism_rate
        parents = np.array([selection_func(pop, scores) for _ in range(num_offspring)])
        
        # Crossover
        offspring_size = (num_offspring, dim)
        offspring = crossover_func(parents, offspring_size, ga_instance)

        # Mutacja
        offspring = mutation_func(offspring, ga_instance)

        pop = np.vstack((new_pop, offspring))

    best_solution = pop[np.argmin([schwefel(ind) for ind in pop])]
    
    end_time = time.time()
    print(f"Czas wykonania algorytmu: {end_time - start_time:.2f} sekundy")
    
    plot_results(history)
    plot_3d_result(best_solution)
    plot_heatmap(best_solution)

    return best_solution
