from matplotlib import pyplot as plt


def plot_results(history):
    plt.plot(history)
    plt.xlabel("Generations")
    plt.ylabel("Best Score")
    plt.show()