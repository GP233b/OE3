import tkinter as tk
from tkinter import ttk
from genetic_algorithm.algorithm import genetic_algorithm
from genetic_algorithm.evaluation import schwefel
from config import POP_SIZE, GENS, MUT_RATE, CROSS_RATE, DIM, X_MIN, X_MAX ,ITERATION

def run_genetic_algorithm(mutation_function, crossover_function, selection_function, mutation_rate, elitism_rate, pop_size, gens, x_min, x_max, dim):
    best_solution = genetic_algorithm(mutation_function, crossover_function, selection_function, mutation_rate, elitism_rate, pop_size, gens, x_min, x_max, dim)
    print("Best solution:", best_solution)
    print("Score:", schwefel(best_solution))

def create_gui():
    root = tk.Tk()
    root.title("Genetic Algorithm Configuration")
    root.geometry("450x550")
    root.resizable(False, False)
    
    style = ttk.Style(root)
    style.theme_use('clam')
    style.configure("TLabel", font=("Helvetica", 10))
    style.configure("TEntry", font=("Helvetica", 10))
    style.configure("TButton", font=("Helvetica", 10, "bold"))
    style.configure("TCombobox", font=("Helvetica", 10))
    
    container = ttk.Frame(root, padding="20 20 20 20")
    container.grid(row=0, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))
    
    r = 0

    ttk.Label(container, text="Select Mutation Function:").grid(row=r, column=0, sticky=tk.W, pady=5)
    mutation_options = ["boundary_mutation", "single_point_mutation", "two_point_mutation", "gaussian_mutation"]
    mutation_combobox = ttk.Combobox(container, values=mutation_options, state="readonly")
    mutation_combobox.grid(row=r, column=1, pady=5, sticky=tk.EW)
    mutation_combobox.set("gaussian_mutation")
    r += 1

    ttk.Label(container, text="Select Crossover Function:").grid(row=r, column=0, sticky=tk.W, pady=5)
    crossover_options = ["one_point_crossover", "two_point_crossover", "uniform_crossover", "granular_crossover"]
    crossover_combobox = ttk.Combobox(container, values=crossover_options, state="readonly")
    crossover_combobox.grid(row=r, column=1, pady=5, sticky=tk.EW)
    crossover_combobox.set("one_point_crossover")
    r += 1

    ttk.Label(container, text="Select Selection Function:").grid(row=r, column=0, sticky=tk.W, pady=5)
    selection_options = ["tournament_selection", "roulette_wheel_selection", "elitist_selection"]
    selection_combobox = ttk.Combobox(container, values=selection_options, state="readonly")
    selection_combobox.grid(row=r, column=1, pady=5, sticky=tk.EW)
    selection_combobox.set("tournament_selection")
    r += 1

    ttk.Label(container, text="Mutation Rate:").grid(row=r, column=0, sticky=tk.W, pady=5)
    mutation_rate_entry = ttk.Entry(container)
    mutation_rate_entry.grid(row=r, column=1, pady=5, sticky=tk.EW)
    mutation_rate_entry.insert(0, str(MUT_RATE))
    r += 1

    ttk.Label(container, text="Elitism Rate (0 for none):").grid(row=r, column=0, sticky=tk.W, pady=5)
    elitism_rate_entry = ttk.Entry(container)
    elitism_rate_entry.grid(row=r, column=1, pady=5, sticky=tk.EW)
    elitism_rate_entry.insert(0, "1")
    r += 1

    ttk.Label(container, text="Population Size (POP_SIZE):").grid(row=r, column=0, sticky=tk.W, pady=5)
    pop_size_entry = ttk.Entry(container)
    pop_size_entry.grid(row=r, column=1, pady=5, sticky=tk.EW)
    pop_size_entry.insert(0, str(POP_SIZE))
    r += 1

    ttk.Label(container, text="Generations (GENS):").grid(row=r, column=0, sticky=tk.W, pady=5)
    gens_entry = ttk.Entry(container)
    gens_entry.grid(row=r, column=1, pady=5, sticky=tk.EW)
    gens_entry.insert(0, str(GENS))
    r += 1

    ttk.Label(container, text="X Min (X_MIN):").grid(row=r, column=0, sticky=tk.W, pady=5)
    x_min_entry = ttk.Entry(container)
    x_min_entry.grid(row=r, column=1, pady=5, sticky=tk.EW)
    x_min_entry.insert(0, str(X_MIN))
    r += 1

    ttk.Label(container, text="X Max (X_MAX):").grid(row=r, column=0, sticky=tk.W, pady=5)
    x_max_entry = ttk.Entry(container)
    x_max_entry.grid(row=r, column=1, pady=5, sticky=tk.EW)
    x_max_entry.insert(0, str(X_MAX))
    r += 1

    ttk.Label(container, text="Dimensions (DIM):").grid(row=r, column=0, sticky=tk.W, pady=5)
    dim_entry = ttk.Entry(container)
    dim_entry.grid(row=r, column=1, pady=5, sticky=tk.EW)
    dim_entry.insert(0, str(DIM))
    r += 1
    
    ttk.Label(container, text="Iteration (ITERATION):").grid(row=r, column=0, sticky=tk.W, pady=5)
    iteration_entry = ttk.Entry(container)
    iteration_entry.grid(row=r, column=1, pady=5, sticky=tk.EW)
    iteration_entry.insert(0, str(ITERATION))
    r += 1

    def on_run_button_click():
        mutation_function = mutation_combobox.get()
        crossover_function = crossover_combobox.get()
        selection_function = selection_combobox.get()
        mutation_rate = float(mutation_rate_entry.get())
        elitism_rate = int(elitism_rate_entry.get())
        pop_size = int(pop_size_entry.get())
        gens = int(gens_entry.get())
        x_min = float(x_min_entry.get())
        x_max = float(x_max_entry.get())
        dim = int(dim_entry.get())
        iteration = int(iteration_entry.get())

        run_genetic_algorithm(mutation_function, crossover_function, selection_function, mutation_rate, elitism_rate, pop_size, gens, x_min, x_max, dim)

    run_button = ttk.Button(container, text="Run Genetic Algorithm", command=on_run_button_click)
    run_button.grid(row=r, column=0, columnspan=2, pady=20)

    for child in container.winfo_children():
        child.grid_configure(padx=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
