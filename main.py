from genetic_algorithm.algorithm import * 

# main.py
if __name__ == "__main__":
    best = genetic_algorithm()
    print("Best solution:", best, "Score:", schwefel(best))