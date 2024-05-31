# Recombination

Recombination, also called crossover, is explorative as it generates a lot of new genetic material.

I am currently only implementing basic crossover methods, namely **n-point crossover** and **uniform crossover**. 
Both of these crossover types are *order-preservation implementations*, meaning that they focus on preserving the order in which genes appear in an individual. 

There are also *adjacency-preservation implementations*, such as **partially mapped crossover (PMX)** and **edge crossover**, which are more advanced but also 
would not really work for binary representations. 

Additionally, other advanced order-preservation implementations are **order crossover** and **cycle crossover**, but these also would not work for 
binary implementations.

## n-point crossover

n-point crossover is exactly like one-point crossover except that instead of splitting the parents at 1 index, they are split at n indices. The n indices are selected randomly.

## Uniform crossover 

Uniform crossover acts like a coinflip for each individual gene in the parents. For each gene, both parents have a 50% chance that their gene will be passed to the offspring.

## Other crossover methods

The crossover methods below are more advanced implementations that would not really work for binary representations.

### PMX

In my **Partially Mapped Crossover (PMX)** example, the two parents will be <ins>123456789</ins> and <ins>567298134</ins>.
The first step in PMX is to randomly select a subset from one of the parents and place it in the corresponding places of the offspring. Let's take the subset <ins>3456</ins> from parent 1, making the offspring <ins>_\_3456\_ _ _</ins>.

Next, we look at which genes from the second parent have not been copied to the offspring, beginning from the left-hand side of parent 1's subset, and copy them over. The algorithm for this is as follows:<br>
For each position *i* in parent 2, we check if *i* is empty in the offspring. If *i* is empty, we copy gene *x* at position *i* in parent 2 into the offspring at position *i*. If, however, *i* is filled in the offspring with gene *y*, we check where *y* appears in parent 2. If *y* appears at position *q* in parent 2, we check to see if *q* is empty in the offspring. If it is, we copy *x* into *q* in the offspring. We repeat this process until an empty position in the offspring is found. If a gene in parent 2 is already in the offspring, we move to the next gene.

<ins>_ \_3456\_ _ _</ins><br>
<ins>567298134</ins><br>

The first instance of this algorithm would be to look index 3. Index 3 of parent 2 has the gene 7. We see that index 3 of the offspring is filled with gene 3. Therefore, we check where 3 appears in parent 2. Gene 3 appears at index 8 of parent 2, and since index 8 of the offspring is empty, we copy gene 7 into index 8 of the offspring.

<ins>_ \_3456\_ 7 _</ins><br>
<ins>567298134</ins><br>

We then continue this process until every location in the offspring has been filled.

The second offspring is generated in the same way, with the roles of the parents reversed.

### Edge crossover

In **edge crossover**, we make an *edge table* of the two parents. This edge table can be thought of as a dictionary of key-value pairs; each key in the dictionary is a gene and the value of the gene is the list of other genes that are adjacent to that gene in both parents.

For example, if two parents were <ins>987654321</ins> and <ins>128934675</ins>, one such key-value pair in the edge table would be {9: 1, 8, 8, 3}.

After constructing the edge table, we randomly select a gene, append it into the offspring, and remove all reference to it from the edge table. Then, looking at the entry for this gene in the edge table and select the next gene to add based on the rules:
1. If there is a common edge (both parents had an adjacency of the genes)
2. The value of the gene's list that itself has the longest list of values
3. Random selection

Once the next gene has been selected, we repeat the process.

NOTE: edge crossover only produces **ONE** offspring.

### Order crossover

The first step of **order crossover** is to copy a random subset of parent 1 into the corresponding location in the offspring. Then, starting from the right-hand end of this subset, copy the genes that are not in the offspring according to the order they appear in the second parent, wrapping around the parent at the end.

The second offspring is generated in the same way, with the roles of the parents reversed.
 
### Cycle crossover

In **cycle crossover**, we divide the parents into *cycles*, which are permutations of subsets of genes of the parent values created based on their relative locations.

We start with the first unused gene, *x*, in parent 1, immediately adding it to the cycle. We then look at the corresponding gene, *y*, in parent 2 and find where *y* occurs in parent 1. After finding where *y* occurs in parent 1, we look at the corresponding gene in parent 2, *z*, and add it to the cycle. We repeat this process until we get back to the gene we started with, *x*, at which point we would add *y* and end the cycle. That is, a cycle that begins with a gene at position *q* in parent 1 *must* end with the gene at position *q* in parent 2.

We then create cycles until every gene is in a cycle.

The construction of the offspring is as follows: for cycle 1, beginning at the first gene of parent 1, we check if that gene is in cycle 1. If it is, add it to the offspring. If it is not, we add the corresponding gene from parent 2. We do this for every cycle, alternating the role of the parents for each cycle.
