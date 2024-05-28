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
