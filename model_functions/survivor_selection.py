import model_functions.fitness_function as fitfunc

# (μ + λ) survivor selection implementation
def mu_plus_lambda(offspring, current_pop):
    total_pop = offspring + current_pop

    # Sort the population by fitness
    pop_and_fit = fitfunc.fitness(total_pop, False)

    return pop_and_fit[:len(current_pop)]
    
# Replacement survivor selection implementation
def replacement(offspring, current_pop):

    # Sort the population by fitness
    sorted_pop = fitfunc.fitness(current_pop, False)

    next_gen = offspring + sorted_pop[len(offspring)+1:]

    return next_gen
