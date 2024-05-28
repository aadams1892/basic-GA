import model_functions.population_initialization as popinit
import model_functions.parent_selection as parselect
import model_functions.recombination as recomb
import model_functions.mutation as mutate
import model_functions.survivor_selection as surselect
import model_functions.fitness_function as fitunc
import random

def ga(pop_size, indiv_length, parent_select, crossover, mutation, survivor_select, optimal_fitness, max_gen, verbose):
    generation = 1
    optimal_fitness_reached = False
    avg_fit = []
    fit_increase = []

    # -=- Population initialization -=-

    pop = popinit.init(pop_size, indiv_length)
    avg_fit.append(fitfunc.total_fitness(pop)/pop_size)
    fit_increase.append(0)
    
    # Genetic algorithm.
    while generation <= max_gen and not optimal_fitness_reached:
        if verbose:
            print("Generation #" + str(generation))

        pop_copy = pop # Copy of population

        # -=- Parent selection -=-

        # Roulette wheel parent selection
        if parent_select[0] == "roulette":
            mp_size = parent_select[1]

            # Check if mating pool size is valid
            if mp_size < 2 or mp_size > len(pop):
                raise ValueError("Invalid mating pool size:", mp_size)
            
            elif mp_size % 2:
                print("WARNING: Non-even mating pool size " + str(mp_size) + ". Decreasing mating pool size to " + str(mp_size-1) + ".")
                mp_size -= 1

            # Get parents
            parents = parselect.roulette_selection(pop, mp_size)
                
        # Tournament parent selection
        elif parent_select[0] == "tournament":
            t_size = parent_select[1]
            mp_size = parent_select[2]

            # Check if mating pool size is valid
            if mp_size < 2 or mp_size > len(pop):
                raise ValueError("Invalid mating pool size:", mp_size)
            
            elif mp_size % 2:
                print("WARNING: Non-even mating pool size " + str(mp_size) + ". Decreasing mating pool size to " + str(mp_size-1) + ".")
                mp_size -= 1

            # Get parents
            parents = parselect.tournament_selection(pop, t_size, mp_size)

        # Invalid parent selection
        else:
            raise ValueError("Invalid parent selection method.")

        # -=- Crossover -=-
        
        raw_offspring = [] # Population of un-mutated offspring
        
        # n-point crossover
        if crossover[0] == "n_point":
            
            n = crossover[1]
            crossover_rate = crossover[2]

            # Go through the entire set of parents
            while len(parents):
                crossover_occurs = random.random() # Random value to determine if crossover occurs

                # Crossover occurs
                if crossover_rate > crossover_occurs:
                    p1 = parents.pop(random.randrange(len(parents)-1))
                    try: p2 = parents.pop(random.randrange(len(parents)-1))
                    except: p2 = parents.pop() # For the case where only 1 parent is left
                    o1, o2 = recomb.n_point_crossover(p1, p2, n)
                    raw_offspring.append(o1)
                    raw_offspring.append(o2)

                # Crossover does not occur, direct copy to offspring
                else:
                    p1 = parents.pop(random.randrange(len(parents)-1))
                    try: p2 = parents.pop(random.randrange(len(parents)-1))
                    except: p2 = parents.pop() # For the case where only 1 parent is left
                    raw_offspring.append(p1)
                    raw_offspring.append(p2)

        # Uniform crossover
        elif crossover[0] == "uniform":
            crossover_rate = crossover[1]

            # Go through the entire set of parents
            while len(parents):
                crossover_occurs = random.random() # Random value to determine if crossover occurs

                # Crossover occurs
                if crossover_rate > crossover_occurs:
                    p1 = parents.pop(random.randrange(len(parents)-1))
                    try: p2 = parents.pop(random.randrange(len(parents)-1))
                    except: p2 = parents.pop() # For the case where only 1 parent is left
                    o1, o2 = recomb.uniform_crossover(p1, p2)
                    raw_offspring.append(o1)
                    raw_offspring.append(o2)

                # Crossover does not occur, direct copy to offspring
                else:
                    p1 = parents.pop(random.randrange(len(parents)-1))
                    try: p2 = parents.pop(random.randrange(len(parents)-1))
                    except: p2 = parents.pop() # For the case where only 1 parent is left
                    raw_offspring.append(p1)
                    raw_offspring.append(p2)
                
        # Invalid crossover
        else:
            raise ValueError("Invalid crossover method.")

        # -=- Mutation -=-

        offspring = [] # Population of offspring

        # Insertion mutation
        if mutation[0] == "insert":
            mutation_rate = mutation[1]

            for i in raw_offspring:
                mutation_occurs = random.random() # Random value to determine if mutation occurs

                # Mutation occurs
                if mutation_rate > mutation_occurs:
                    mutated_i = mutate.insertion_mutation(i)
                    offspring.append(mutated_i)

                # Mutation does not occur, direct copy of individual
                else:
                    offspring.append(i)

        # Scramble mutation
        elif mutation[0] == "scramble":
            subset_range = mutation[1]
            mutation_rate = mutation[2]

            for i in raw_offspring:
                mutation_occurs = random.random() # Random value to determine if mutation occurs

                # Mutation occurs
                if mutation_rate > mutation_occurs:
                    mutated_i = mutate.scramble_mutation(i, subset_range)
                    offspring.append(mutated_i)

                # Mutation does not occur, direct copy of individual
                else:
                    offspring.append(i)

        # Inversion mutation
        elif mutation[0] == "invert":
            subset_range = mutation[1]
            mutation_rate = mutation[2]

            for i in raw_offspring:
                mutation_occurs = random.random() # Random value to determine if mutation occurs

                # Mutation occurs
                if mutation_rate > mutation_occurs:
                    mutated_i = mutate.inversion_mutation(i, subset_range)
                    offspring.append(mutated_i)

                # Mutation does not occur, direct copy of individual
                else:
                    offspring.append(i)

        # Invalid mutation
        else:
            raise ValueError("Invalid mutation method.")
    
        # -=- Survivor selection -=-
        
        # (μ + λ) survivor selection
        if survivor_select[0] == "mu_plus_lambda":
            pop = surselect.mu_plus_lambda(offspring, pop_copy)

        # Replacement survivor selection
        elif survivor_select[0] == "replacement":
            pop = surselect.replacement(offspring, pop_copy)
        
        # Invalid survivor selection
        else:
            raise ValueError("Invalid survivor selection method.")

        # -=- Collect generation info -=-

        # Total fitness
        avg_fit.append(round(fitfunc.total_fitness(pop)/pop_size, 3))

        # Increase in average fitness
        fit_increase.append(round(avg_fit[generation] - avg_fit[generation-1], 3))

        if verbose:
            print("Average fitness:", avg_fit[generation])
            print("Fitness increase from previous generation:", fit_increase[generation])
            print("Highest fitness:", fitfunc.fitness(pop[0], True))
            print("\n")

        # -=- Check termination condition -=-
        
        # Since the population will always be sorted, we can check the first individual to see if it has reached optimal fitness.

        if fitfunc.fitness(pop[0], True) >= optimal_fitness:
            optimal_fitness_reached = True

        else:
            generation += 1

    gens_needed = generation # Generations needed
    avg_increase_in_avg_fit = 0
    for fit_inc in fit_increase:
        avg_increase_in_avg_fit += fit_inc

    avg_increase_in_avg_fit = round(avg_increase_in_avg_fit/gens_needed, 3) # Average increase in the average fitness of the generation
    
    # Optimal fitness reached
    if optimal_fitness_reached:
        print("Optimal fitness reached!")
        return [fitfunc.fitness(pop[0], True), gens_needed, avg_increase_in_avg_fit, avg_fit, fit_increase[1:]]

    # Maximum generations reached
    else:
        print("Max generation reached.")
        return [fitfunc.fitness(pop[0], True), generation-1, avg_increase_in_avg_fit, avg_fit, fit_increase[1:]]
