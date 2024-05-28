# DEBUG
insert = 1
scramble = 0
invert = 0
DEBUG = 0

# Insertion mutation implementation
def insertion_mutation(indiv):
    # Get random genes
    gene1 = random.randrange(len(indiv))
    gene2 = random.randrange(len(indiv))

    # Get a new gene if the genes are equal or already next to each other
    while gene1 == gene2 or gene1 == gene2-1 or gene1 == gene2+1:
        gene2 = random.randrange(len(indiv))

    if DEBUG:
        print(gene1, gene2)

    # Case gene1 > gene2. Move gene1 back to be next to gene2.
    if gene1 > gene2:
        mutated_indiv = indiv[:gene2+1] + [indiv[gene1]] + indiv[gene2+1:gene1] + indiv[gene1+1:]

    # Case gene2 > gene1. Move gene2 to be next to gene1.
    else:
        mutated_indiv = indiv[:gene1+1] + [indiv[gene2]] + indiv[gene1+1:gene2] + indiv[gene2+1:]

    return mutated_indiv


# Scramble mutation implementation
def scramble_mutation(indiv, subset_size_range):
    # Get the two indices of the subset
    gene1 = random.randint(0, len(indiv)-1)
    gene2 = random.randint(0, len(indiv)-1)

    # Check that the subset size is in range
    while abs(gene1 - gene2) < subset_size_range[0] or abs(gene1 - gene2) > subset_size_range[1]:
        gene2 = random.randint(0, len(indiv)-1)

    # Case gene1 > gene2. The subset will wrap around the individual
    if gene1 > gene2:
        subset1 = indiv[gene1:]
        subset2 = indiv[:gene2+1]

        if DEBUG:
            print(subset1)
            print(subset2)

        # Randomly scramble the subsets
        random.shuffle(subset1)
        random.shuffle(subset2)
        mutated_indiv = subset2 + indiv[gene2+1:gene1] + subset1

    # Case gene2 > gene1. No wraparound
    else:
        subset = indiv[gene1:gene2+1]

        if DEBUG:
            print(subset)

        # Randomly scramble the subset
        random.shuffle(subset)
        mutated_indiv = indiv[:gene1] + subset + indiv[gene2+1:]

    return mutated_indiv


# INVERSION MUTATION CODE LARGELY TAKEN FROM MY CISC499 PROJECT REPO ON GITHUB

# Inversion mutation implementation
def inversion_mutation(indiv, subset_size_range):

    # Randomly choose indicesd
    inversion_start = random.randint(0, len(indiv)-1)
    inversion_end = random.randint(0, len(indiv)-1)

    # Ensure the inversion ends are different genes
    while inversion_end == inversion_start:
        inversion_end = random.randint(0, len(indiv)-1)

    # Check that the subset size is in range
    while abs(inversion_start - inversion_end) < subset_size_range[0] or abs(inversion_start - inversion_end) > subset_size_range[1]:
        inversion_end = random.randint(0, len(indiv)-1)
   
    if DEBUG:
        print(inversion_start, inversion_end)

    # The inversion will wrap around the individual
    if inversion_end < inversion_start:
        inversion_subset1 = indiv[inversion_start:]
        inversion_subset2 = indiv[:inversion_end+1]
        inversion_subset = inversion_subset1 + inversion_subset2

        if DEBUG:
            print("Original subset:", inversion_subset)
            
        inversion_subset.reverse() # Reverse the subset

        index_split = len(indiv) - inversion_start

        # Replace original individual with inverted subset.
        # Take the first index_split elements of the inversion_subset, since these will be the 'last' elements of the inversion.
        # We then take the part of the individual that was not mutated.
        # We then take the last index_split elements from the mutated subset, since these were the 'first' elements in the
        # inverted subset.
        mutated_indiv = inversion_subset[index_split:] + indiv[inversion_end+1:inversion_start] + inversion_subset[:index_split]
        
    # No wrap around
    else:
        if DEBUG:
            print("Original subset:", indiv[inversion_start:inversion_end+1])

        inversion_subset = indiv[inversion_start:inversion_end+1]
        inversion_subset.reverse() # Reverse the subset
        mutated_indiv = indiv[:inversion_start] + inversion_subset + indiv[inversion_end+1:]

    if DEBUG:
        print("Inverted subset:", inversion_subset)

    return mutated_indiv


if DEBUG:
    if insert:
        print(insert_mutation([0,1,1,0,1,0,0,1,0]))
    elif scramble:
        print(scramble_mutation([0,1,2,3,4,5,6,7,8]))
    elif invert:
        print(inversion_mutation([0,1,2,3,4,5,6,7,8]))
    else:
        raise ValueError("No mutation method specified.")
    
