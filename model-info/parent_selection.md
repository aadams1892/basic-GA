# Parent Selection

The two most widely used methods of parent selection are **roulette wheel selection** and **tournament selection**.
Both are implementations of *fitness-proportional selection (FPS)*, whereby individuals are compared according to their fitness.
Downsides of FPS are that a highly fit individual can quickly dominate the landscape, leading to premature convergence. 
I find that a way to avoid this is using tournament selection with a large tournament size to keep selection pressure high.

## Roulette Wheel Selection

In roulette wheel selection, we calculate the total fitness of the entire population, select a target fitness, and cumulatively add the fitness of each individual
until we reach the target fitness. The individual whose fitness brings the cumulative fitness beyond the target fitness is selected as the parent. 
We then add this parent to a mating pool and repeat this process until the mating pool is full. 
Individuals in the mating pool are selected to produce offspring.

## Tournament Selection

In tournament selection, in addition to the mating pool size, we also specify a tournament size, *x*. 
In each iteration of the function, we randomly select a subset of individuals of size *x* and rank them using the fitness function, with the highest fitness
individual having rank 1. We then deterministically select the 2 fittest individuals to be the parents and move them to the mating pool. 
We repeat this process until we have filled the mating pool. We then select parents from the mating pool to produce offspring.
