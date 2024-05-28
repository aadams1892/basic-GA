# basic-GA
This repository contains basic genetic algorithm (GA) implementations for parent selection, recombination, mutation, and survivor selection. It is meant to provide a convenient way to compare the performance of different combinations of GA methods.

# Running the GA
To run the GA, open the main.py file and set the function implementations you want the GA to have and then run the file.
One of the arguments into the GA is **verbose** which, when active, will print out basic information for each generation. If it is not active, only the final GA state will be output.

In addition to text output, the GA will also display two figures, one of the average fitness of the population for each generation and one for the change in average fitness for each generation from the previous generation.

# Model Functions
The code for the functions used in the GA and the GA file itself are in the model_functions folder.

# Model Info
The model_info folder contains information about the GA functions implemented as well as some brief information on additional implementations.

# Implementation Options
All currently available function implementations are listed in the GA_options.md file. The naming convention, any hyperparameters, and correct format for each implementation is listed.
