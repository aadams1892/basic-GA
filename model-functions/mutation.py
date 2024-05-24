DEBUG = 0
insert = 0
scramble = 1
invert = 0

# Insert mutation implementation
def insert_mutation(indiv):
    gene1 = random.randint(0, len(indiv)-1)
    gene2 = random.randint(0, len(indiv)-1)

    # Get a new gene if the genes are equal or already next to each other
    while gene1 == gene2 or gene1 == gene2-1 or gene1 == gene2+1:
        gene2 = random.randint(0, len(indiv)-1)

    if DEBUG:
        print(gene1, gene2)

    # Case gene1 > gene2. Move gene1 back to be next to gene2.
    if gene1 > gene2:
        g1 = indiv.pop(gene1) # Remove gene1 from the individual
        if DEBUG:
            print(g1)
            print(indiv)
        mutated_indiv = indiv[:gene2] + [indiv[gene2], g1] + indiv[gene2+1:]


    # Case gene2 > gene1. Move gene2 to be next to gene1.
    else:
        g2 = indiv.pop(gene2)
        if DEBUG:
            print(g2)
            print(indiv)
        mutated_indiv = indiv[:gene1] + [indiv[gene1], g2] + indiv[gene1+1:]
    
    return mutated_indiv


# Scramble mutation implementation
def scramble_mutation(indiv, subset_size_range):
    # Get the two indices of the subset
    gene1 = random.randint(0, len(indiv)-1)
    gene2 = random.randint(0, len(indiv)-1)

    # Check that the subset size is in range
    while abs(gene1 - gene2) < subset_size_range[0] or abs(gene1 - gene2) > subset_size_range[1]:
        gene2 = random.randint(0, len(indiv)-1)

    # Case gene1 > gene2
    if gene1 > gene2:
        subset1 = indiv[gene1:]
        subset2 = indiv[:gene2+1]

        if DEBUG:
            print(subset1)
            print(subset2)

        random.shuffle(subset1)
        random.shuffle(subset2)
        mutated_indiv = subset2 + indiv[gene2+1:gene1] + subset1

    # Case gene2 > gene1
    else:
        subset = indiv[gene1:gene2+1]

        if DEBUG:
            print(subset)

        random.shuffle(subset)
        mutated_indiv = indiv[:gene1] + subset + indiv[gene2+1:]

    return mutated_indiv


# INVERSION MUTATION CODE TAKEN FROM MY CISC499 PROJECT REPO

# Inversion mutation implementation
def inversion_mutation(indiv, subset_size_range):
    # Performs Inversion Mutation on an individual

    # Indices randomly chosen such that they cannot equal each other
    inversion_start = random.randint(0, len(indiv)-1)
    inversion_end = random.randint(0, len(indiv)-1)

    # Check that the subset size is in range
    while abs(inversion_start - inversion_end) < subset_size_range[0] or abs(inversion_start - inversion_end) > subset_size_range[1]:
        inversion_end = random.randint(0, len(indiv)-1)
   
    if DEBUG:
        print(inversion_start, inversion_end)

    if inversion_end < inversion_start:
        inversion_subset1 = indiv[inversion_start:]
        inversion_subset2 = indiv[:inversion_end+1]
        inversion_subset = inversion_subset1 + inversion_subset2

        if DEBUG:
            print("Original subset:", inversion_subset)
            
        inversion_subset.reverse() # Reverse the subset.

        index_split = len(indiv) - inversion_start

        # Replace original individual with inverted subset.
        # Take the first index_split elements of the inversion_subset, since these will be the 'last' elements of the inversion.
        # We then take the part of the individual that was not mutated.
        # We then take the last index_split elements from the mutated subset, since these were the 'first' elements in the
        # inverted subset.
        mutated_indiv = inversion_subset[index_split:] + indiv[inversion_end+1:inversion_start] + inversion_subset[:index_split]

    else:
        # No wrap around
        if DEBUG:
            print("Original subset:", indiv[inversion_start:inversion_end+1])

        inversion_subset = indiv[inversion_start:inversion_end+1]
        inversion_subset.reverse()
        mutated_indiv = indiv[:inversion_start] + inversion_subset + indiv[inversion_end+1:]

    if DEBUG:
        print("Inverted subset:", inversion_subset)

    return mutated_indiv


if DEBUG:
    if insert:
        print(insert_mutation([0,1,2,3,4,5,6,7,8]))
    elif scramble:
        print(scramble_mutation([0,1,2,3,4,5,6,7,8]))
    elif invert:
        print(inversion_mutation([0,1,2,3,4,5,6,7,8]))
    else:
        raise ValueError("No mutation method specified.")
