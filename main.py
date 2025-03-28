from genetic_algorithm.algorithm import * 

if __name__ == "__main__":
    best = genetic_algorithm()
    print("Best solution:", best, "Score:", schwefel(best))