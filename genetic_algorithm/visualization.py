from matplotlib import pyplot as plt

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