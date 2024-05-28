# GA Options

Below is a list of the hyperparameters and available implementations for the genetic algorithm functions.

#### Parent Selection
- "roulette"
    - Hyperparameters: mating_pool_size
    - Format: parent_selection = ["roulette", mating_pool_size]
- "tournament"
    - Hyperparameters: tournament_size, mating_pool_size
    - Format: ["tournament", tournament_size, mating_pool_size]

#### Crossover
- "n_point"
    - Hyperparameters: n, crossover_rate
    - Format: ["n_point", n, crossover_rate]
- "uniform"
    - Hyperparameters: crossover_rate
    - Format: ["uniform", crossover_rate]

#### Mutation
- "insert"
    - Hyperparameters: mutation_rate
    - Format: ["insert", mutation_rate]
- "scramble"
    - Hyperparameters: subset_size_range, mutation_rate
    - Format: ["scramble", [min_subset_size, max_subset_size], mutation_rate]
- "invert"
    - Hyperparameters: subset_size_range, mutation_rate
    - Format: ["invert", [min_subset_size, max_subset_size], mutation_rate]

#### Survivor Selection
- "mu_plus_lambda"
    - Hyperparameters: None
    - Format: ["mu_plus_lambda"]
- "replacement"
    - Hyperparameters: None
    - Format: ["replacement"]
