import tkinter as tk
from tkinter import ttk
from genetic_algorithm.algorithm import genetic_algorithm
from genetic_algorithm.evaluation import schwefel
from config import POP_SIZE, GENS, MUT_RATE, CROSS_RATE, DIM, X_MIN, X_MAX

def run_genetic_algorithm(mutation_function, crossover_function, selection_function, mutation_rate, elitism_rate, pop_size, gens, x_min, x_max, dim):
    best_solution = genetic_algorithm(mutation_function, crossover_function, selection_function, mutation_rate, elitism_rate, pop_size, gens, x_min, x_max, dim)
    print("Best solution:", best_solution)
    print("Score:", schwefel(best_solution))

def create_gui():
    root = tk.Tk()
    root.title("Genetic Algorithm Configuration")
    root.geometry("500x600")
    root.resizable(False, False)
    root.configure(bg="#2c3e50")
    
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TLabel", font=("Helvetica", 11), background="#2c3e50", foreground="white")
    style.configure("TEntry", font=("Helvetica", 11))
    style.configure("TButton", font=("Helvetica", 11, "bold"), background="#16a085", foreground="white")
    style.configure("TCombobox", font=("Helvetica", 11))
    
    container = ttk.Frame(root, padding="20 20 20 20", relief="ridge", borderwidth=3)
    container.grid(row=0, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))
    
    r = 0
    def create_label(text):
        return ttk.Label(container, text=text)
    
    def create_entry(default_value):
        entry = ttk.Entry(container)
        entry.insert(0, str(default_value))
        return entry
    
    create_label("Select Mutation Function:").grid(row=r, column=0, sticky=tk.W, pady=5)
    mutation_combobox = ttk.Combobox(container, values=["boundary_mutation", "single_point_mutation", "two_point_mutation", "gaussian_mutation"], state="readonly")
    mutation_combobox.grid(row=r, column=1, pady=5, sticky=tk.EW)
    mutation_combobox.set("gaussian_mutation")
    r += 1
    
    create_label("Select Crossover Function:").grid(row=r, column=0, sticky=tk.W, pady=5)
    crossover_combobox = ttk.Combobox(container, values=["one_point_crossover", "two_point_crossover", "uniform_crossover", "granular_crossover"], state="readonly")
    crossover_combobox.grid(row=r, column=1, pady=5, sticky=tk.EW)
    crossover_combobox.set("one_point_crossover")
    r += 1
    
    create_label("Select Selection Function:").grid(row=r, column=0, sticky=tk.W, pady=5)
    selection_combobox = ttk.Combobox(container, values=["tournament_selection", "roulette_wheel_selection", "elitist_selection"], state="readonly")
    selection_combobox.grid(row=r, column=1, pady=5, sticky=tk.EW)
    selection_combobox.set("tournament_selection")
    r += 1
    
    entries = {
        "Mutation Rate:": MUT_RATE,
        "Elitism Rate (0 for none):": 1,
        "Population Size (POP_SIZE):": POP_SIZE,
        "Generations (GENS):": GENS,
        "X Min (X_MIN):": X_MIN,
        "X Max (X_MAX):": X_MAX,
        "Dimensions (DIM):": DIM,
    }
    entry_widgets = {}
    
    for label, default in entries.items():
        create_label(label).grid(row=r, column=0, sticky=tk.W, pady=5)
        entry = create_entry(default)
        entry.grid(row=r, column=1, pady=5, sticky=tk.EW)
        entry_widgets[label] = entry
        r += 1
    
    def on_run_button_click():
        run_genetic_algorithm(
            mutation_combobox.get(),
            crossover_combobox.get(),
            selection_combobox.get(),
            float(entry_widgets["Mutation Rate:"].get()),
            int(entry_widgets["Elitism Rate (0 for none):"].get()),
            int(entry_widgets["Population Size (POP_SIZE):"].get()),
            int(entry_widgets["Generations (GENS):"].get()),
            float(entry_widgets["X Min (X_MIN):"].get()),
            float(entry_widgets["X Max (X_MAX):"].get()),
            int(entry_widgets["Dimensions (DIM):"].get())
        )
    
    run_button = ttk.Button(container, text="Run Genetic Algorithm", command=on_run_button_click)
    run_button.grid(row=r, column=0, columnspan=2, pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
