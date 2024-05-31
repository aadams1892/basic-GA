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

The crossover methods below are more advanced implementations that would not really work for binary representations. When I say they are more advanced, I am referring to the algorithms to implement them being more complex than the ones listed above. The best way, in my opinion, to be able to explain these implementations is to use an example in the explanation.

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

We then continue this process:

<ins>_ \_3456\_ 72</ins><br>
<ins>567298134</ins><br>

<ins>9\_3456\_ 72</ins><br>
<ins>567298134</ins><br>

<ins>983456\_72</ins><br>
<ins>567298134</ins><br>

<ins>983456172</ins><br>
<ins>567298134</ins><br>

The second offspring is generated in the same way, with the roles of the parents reversed.

### Edge crossover

### Order crossover

### Cycle crossover
