from config import *
from genetic_algorithm.evaluation import schwefel
from genetic_algorithm.mutation import *
from genetic_algorithm.crossover import *
from genetic_algorithm.selection import *
from genetic_algorithm.visualization import plot_3d_result, plot_heatmap, plot_results

def genetic_algorithm(mutation_function, crossover_function, selection_function, mutation_rate):
    # Get the function objects dynamically using getattr
    mutation_func = globals()[mutation_function]
    crossover_func = globals()[crossover_function]
    selection_func = globals()[selection_function]

    pop = np.random.uniform(X_MIN, X_MAX, (POP_SIZE, DIM))
    history = []
    
    for _ in range(GENS):
        scores = np.array([schwefel(ind) for ind in pop])
        best_score = np.min(scores)
        history.append(best_score)
        new_pop = []
        
        for _ in range(POP_SIZE // 2):
            p1, p2 = selection_func(pop, scores), selection_func(pop, scores)
            c1, c2 = crossover_func(p1, p2) if np.random.rand() < CROSS_RATE else (p1, p2)
            new_pop.extend([mutation_func(c1, mutation_rate), mutation_func(c2, mutation_rate)])

        pop = np.array(new_pop)

    best_solution = pop[np.argmin([schwefel(ind) for ind in pop])]
    plot_results(history)
    plot_3d_result(best_solution)
    plot_heatmap(best_solution)
    
    return best_solution