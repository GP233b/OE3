import tkinter as tk
from tkinter import ttk
from genetic_algorithm.algorithm import genetic_algorithm
from genetic_algorithm.evaluation import schwefel

def run_genetic_algorithm(mutation_function, crossover_function, selection_function, mutation_rate):
    # Run the genetic algorithm with the selected functions and mutation rate
    best_solution = genetic_algorithm(mutation_function, crossover_function, selection_function, mutation_rate)
    print("Best solution:", best_solution)
    print("Score:", schwefel(best_solution))

def create_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Genetic Algorithm Configuration")

    # Create labels and dropdowns for mutation, crossover, and selection functions
    tk.Label(root, text="Select Mutation Function").grid(row=0, column=0)
    mutation_options = ["boundary_mutation", "single_point_mutation", "two_point_mutation", "gaussian_mutation"]
    mutation_combobox = ttk.Combobox(root, values=mutation_options)
    mutation_combobox.grid(row=0, column=1)
    mutation_combobox.set("gaussian_mutation")

    tk.Label(root, text="Select Crossover Function").grid(row=1, column=0)
    crossover_options = ["one_point_crossover", "two_point_crossover", "uniform_crossover", "granular_crossover"]
    crossover_combobox = ttk.Combobox(root, values=crossover_options)
    crossover_combobox.grid(row=1, column=1)
    crossover_combobox.set("one_point_crossover")

    tk.Label(root, text="Select Selection Function").grid(row=2, column=0)
    selection_options = ["tournament_selection", "roulette_wheel_selection", "elitist_selection"]
    selection_combobox = ttk.Combobox(root, values=selection_options)
    selection_combobox.grid(row=2, column=1)
    selection_combobox.set("tournament_selection")

    tk.Label(root, text="Mutation Rate").grid(row=3, column=0)
    mutation_rate_entry = tk.Entry(root)
    mutation_rate_entry.grid(row=3, column=1)
    mutation_rate_entry.insert(0, "0.05")  # Default mutation rate

    # Define the run button to execute the genetic algorithm with selected options
    def on_run_button_click():
        mutation_function = mutation_combobox.get()
        crossover_function = crossover_combobox.get()
        selection_function = selection_combobox.get()
        mutation_rate = float(mutation_rate_entry.get())
        run_genetic_algorithm(mutation_function, crossover_function, selection_function, mutation_rate)

    run_button = tk.Button(root, text="Run Genetic Algorithm", command=on_run_button_click)
    run_button.grid(row=4, column=0, columnspan=2)

    root.mainloop()