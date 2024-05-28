import numpy as np

# Merge sort
def merge(left, right):

    left_index = 0
    right_index = 0
    # Sorted population
    sorted = []
    # Compare fitnessess
    while left_index < len(left) and right_index < len(right):

        # Left fitness is higher or equal
        if left[left_index][1] >= right[right_index][1]:
            sorted.append(left[left_index])
            left_index += 1

        # Right fitness is higher
        else:
            sorted.append(right[right_index])
            right_index += 1

    # Add remaining individuals in the left side, if any
    while left_index < len(left):
        sorted.append(left[left_index])
        left_index += 1

    # Add remaining individuals in the right side, if any
    while right_index < len(right):
        sorted.append(right[right_index])
        right_index += 1

    return sorted

# Sort function
def sort(pop_fit):

    if len(pop_fit) == 1:
        return pop_fit
    
    mid = len(pop_fit)//2
    left_arr = sort(pop_fit[:mid])
    right_arr = sort(pop_fit[mid:])

    sorted_pop = merge(left_arr, right_arr)

    return sorted_pop
        
# Fitness function
def fitness(pop, single):
    
    # No population, raise error
    if len(pop) == 0:
        raise ValueError("Empty population.")

    # Getting fitness for only 1 individual
    elif single == True:
        return np.count_nonzero(np.array(pop) == 1)
    
    # Getting fitness for multiple individuals and then sorting them
    else:
        pop_and_fit = []
        for i in pop:
            pop_and_fit.append([i, np.count_nonzero(np.array(i) == 1)])
    
        sorted_pop_and_fit = sort(pop_and_fit)
        sorted_pop = []

        # Get just the individuals
        for i in sorted_pop_and_fit:
            sorted_pop.append(i[0])

        return sorted_pop

# Calculate fitness of entire population
def total_fitness(pop):
    
    total_fit = 0
    for i in pop:
        total_fit += fitness(i, True)

    return total_fit
