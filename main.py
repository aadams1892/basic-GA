# ADD IMPORTS TO ALL FILES AS NEEDED

pop_size = 1000
indiv_len = 150
parent_selection = ["roulette", 10]
crossover_spec = ["uniform", 0.85]
mutation_spec = ["scramble", [2, 6], 0.8]
survivor_selection = ["mu_plus_lambda"]
optimal_fitness = indiv_len
max_gen = 250
verbose = 0 # If you want extended information about each generation

g = ga(pop_size, indiv_len, parent_selection, crossover_spec, mutation_spec, survivor_selection, optimal_fitness, max_gen, verbose)
print("Highest fitness:", g[0])
print("Generations simulated:", g[1])
print("Average fitness increase each generation:", g[2])
print("Starting average fitness:", g[3][0])
print("Ending average fitness:", g[3][1])
