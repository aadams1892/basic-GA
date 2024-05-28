import numpy as np
import random

# n-point crossover implementation
def n_point_crossover(p1, p2, n):
    n_indices = []
    # Get the crossover indices
    while len(n_indices) < n:
        crossover_index = random.randint(1, len(p1)-1) # Bounds set to 1 and len(p1)-1 to ensure that the index actually has an effect on the offspring
        if crossover_index not in n_indices:
            n_indices.append(crossover_index)

    # Sorts the indices to ensure no errors.
    n_indices = np.sort(n_indices)

    # Create offspring
    # Add first subset
    offspring1 = p1[:n_indices[0]]
    offspring2 = p2[:n_indices[0]]

    # Add all but last subset
    for index in range(1, len(n_indices)):
        # Odd crossover point
        if index % 2:
            offspring1 = offspring1 + p2[n_indices[index-1]:n_indices[index]]
            offspring2 = offspring2 + p1[n_indices[index-1]:n_indices[index]]

        # Even crossover point
        else:
            offspring1 = offspring1 + p1[n_indices[index-1]:n_indices[index]]
            offspring2 = offspring2 + p2[n_indices[index-1]:n_indices[index]]

    # Add last subset
    # Odd crossover point
    if len(n_indices) % 2:
        offspring1 = offspring1 + p2[n_indices[-1]:]
        offspring2 = offspring2 + p1[n_indices[-1]:]

    # Even crossover point
    else:
        offspring1 = offspring1 + p1[n_indices[-1]:]
        offspring2 = offspring2 + p2[n_indices[-1]:]

    return offspring1, offspring2

# Uniform crossover implementation
def uniform_crossover(p1, p2):
    offspring1 = []
    offspring2 = []

    # Coinflip to determine which parent's gene is inherited by each offspring
    for i in range(len(p1)):
        coinflip = random.randint(1,2)

        # Give offspring gene from p1
        if coinflip == 1:
            offspring1.append(p1[i])
            offspring2.append(p2[i])

        # Give offspring gene from p2
        else:
            offspring1.append(p2[i])
            offspring2.append(p1[i])

    return offspring1, offspring2
