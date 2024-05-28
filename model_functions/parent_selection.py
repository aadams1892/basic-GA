import model_functions.fitness_function as fitfunc
# DEBUG
roulette = 1
tournament = 0
DEBUG = 0

# Roulette wheel parent selection implementation
def roulette_selection(pop, mp_size):
    total_fit = fitfunc.total_fitness(pop) # Get the total population's fitness
    target_fit = random.randint(1, total_fit) # Select a random value in the range of the total fitness that will determine which individual is selected
    cumulative_fit = 0 # Cumulative fitness of currently added individuals
    indiv_index = 0
    parent_found = False
    mating_pool = []

    # Fill the mating pool
    while len(mating_pool) < mp_size:

        if DEBUG:
            print("Total:", total_fit, "Target:", target_fit)

        # Find the selected individual.
        while not parent_found and indiv_index < len(pop):

            # Add the next individual's fitness to the cumulative total
            cumulative_fit += fitfunc.fitness(pop[indiv_index], True)

            if DEBUG:
                print("Individual:", indiv_index, "Cumulative fitness:", cumulative_fit)

            # Check if we have surpassed the selected fitness
            if cumulative_fit >= target_fit:
                # Found parent

                if DEBUG:
                    print("Parent found.")

                parent = pop[indiv_index]
                parent_found = True

            # Otherwise, go to the next individual
            indiv_index += 1
            
            if indiv_index == len(pop) and not parent_found:
                print("ERROR: Parent not found.")
                break

        # Add the individual to the mating pool
        mating_pool.append(parent)
        indiv_index = 0
        parent_found = False

    # Return the filled mating pool
    return mating_pool


# Tournament parent selection implementation
def tournament_selection(pop, tournament_size, mp_size):
    tourn_pop = [] # Tournament subset
    fittest = [[None, 0], [None, 0]] # The two fittest individuals
    mating_pool = []

    # Fill the mating pool
    while len(mating_pool) < mp_size:

        # Get tournament subset
        while len(tourn_pop) < tournament_size:
            indiv_to_add = pop[random.randint(0, len(pop)-1)]
            tourn_pop.append(indiv_to_add)

        # Rank individuals in tournament
        for i in tourn_pop:
            indiv_fit = fitfunc.fitness(i, True)

            # Check if they are one of the fittest
            if indiv_fit > fittest[0][1]:
                fittest[0] = [i, indiv_fit]
            elif indiv_fit > fittest[1][1]:
                fittest[1] = [i, indiv_fit]

        # Place winners into mating pool
        mating_pool.append(fittest[0][0])
        mating_pool.append(fittest[1][0])

    return mating_pool


if DEBUG:
    population = init(25, 10)
    # Roulette wheel
    if roulette:
        parent1 = roulette_selection(population)
        parent2 = roulette_selection(population)

    # Tournament
    elif tournament:
        mp = tournament_selection(population, 5, 20)
        # Parents are then randomly selected from the mating pool to generate offspring

    # No parent selection specified
    else:
        raise ValueError("No parent selection method specified.")
