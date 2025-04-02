import matplotlib.pyplot as plt
from genetic_algorithm.visualization import plot_3d_result, plot_heatmap, plot_results


def save_iteration_graph(history, best_solution, iteration):

    plot_results(history, filename=f"iteration_graphs/results_{iteration}.png")

    plot_3d_result(best_solution, filename=f"iteration_graphs/best_solution_3d_{iteration}.png")

    plot_heatmap(best_solution, filename=f"iteration_graphs/heatmap_{iteration}.png")
