import random

# Initialize population
def init(pop_size, indiv_length):
    indiv = []
    population = []
    # Create population of individuals
    for i in range(pop_size):
        for _ in range(indiv_length):
            # Add either a 0 or 1 to the individual
            indiv.append(random.randint(0,1))
        # Add the individual to the population
        population.append(indiv)
        # Reset individual
        indiv = []

    return population
