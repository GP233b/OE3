from matplotlib import pyplot as plt
import numpy as np

from genetic_algorithm.evaluation import schwefel

def plot_results(history, filename="results.jpg"):
    plt.figure(figsize=(8, 6))
    plt.plot(history, label="Best Score", color="blue", linewidth=2)
    plt.xlabel("Generations")
    plt.ylabel("Best Score")
    plt.title("Genetic Algorithm Optimization")
    plt.legend()
    plt.grid(True)
    plt.savefig(filename, format="jpg")
    plt.close()

def plot_3d_result(best_solution, filename="best_solution_3d.jpg"):
    x, y = best_solution
    z = schwefel(best_solution)
    
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    X = np.linspace(-500, 500, 100)
    Y = np.linspace(-500, 500, 100)
    X, Y = np.meshgrid(X, Y)
    Z = schwefel([X, Y])

    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)

    ax.scatter(x, y, z, color='red', s=100, label='Best Solution')

    ax.set_title("Best Solution on Schwefel Function")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend()

    plt.savefig(filename, format="jpg")
    plt.close()

def plot_heatmap(best_solution, filename="heatmap.jpg"):
    x, y = best_solution
    
    X = np.linspace(-500, 500, 200)
    Y = np.linspace(-500, 500, 200)
    X, Y = np.meshgrid(X, Y)
    Z = schwefel([X, Y])

    plt.figure(figsize=(8, 6))
    plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar(label="Schwefel Value")

    plt.scatter(x, y, color='red', s=100, label='Best Solution')
    plt.title("Heatmap of Schwefel Function with Best Solution")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()

    plt.savefig(filename, format="jpg")
    plt.close()