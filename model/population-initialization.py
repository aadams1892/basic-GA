# Initializing a population
import random
DEBUG = 0

def init(pop_size, indiv_length):
    indiv = []
    population = []
    # Create population of individuals
    for i in range(pop_size):
        for _ in range(indiv_length):
            indiv.append(random.randint(0,1))
        population.append(indiv)
        indiv = []

    return population

if DEBUG:
    test_pop = init(10, 10)
    print(test_pop)
