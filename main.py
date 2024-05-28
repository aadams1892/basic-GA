from matplotlib import pyplot as mpp
import numpy as np
import genetic_algorithm as genalg

# GA parameters
pop_size = 10000
indiv_len = 250
parent_selection = ["tournament", 100, 100]
crossover_spec = ["n_point", 15, 0.9]
mutation_spec = ["scramble", [50, 75], 0.9]
survivor_selection = ["mu_plus_lambda"]
optimal_fitness = indiv_len
max_gen = 300
verbose = 1 # If you want extended information about each generation

g = genalg.ga(pop_size, indiv_len, parent_selection, crossover_spec, mutation_spec, survivor_selection, optimal_fitness, max_gen, verbose)
print("Highest fitness:", g[0])
print("Generations simulated:", g[1])
print("Average fitness increase each generation:", g[2])
print("Starting average fitness:", g[3][0])
print("Ending average fitness:", g[3][-1])

# Average fitness per generation
fig1 = mpp.figure()
mpp.plot(np.arange(0, g[1]+1, 1), g[3])

# Average fitness increase per generation
fig2 = mpp.figure()
mpp.plot(np.arange(1, g[1]+1, 1), g[4])

# Show figures
mpp.show()
