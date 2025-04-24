import random
import numpy as np
import matplotlib.pyplot as plt
import time

class KnapsackGA:
    def __init__(self, items, weights, values, max_weight, population_size=100, generations=100, 
                 mutation_rate=0.1, crossover_rate=0.8, elitism=2):
        """
        Initialize the Genetic Algorithm for solving the Knapsack Problem
        
        Parameters:
        - items: list of item names
        - weights: list of item weights
        - values: list of item values
        - max_weight: maximum weight capacity of the knapsack
        - population_size: size of the population in each generation
        - generations: number of generations to evolve
        - mutation_rate: probability of mutation for each gene
        - crossover_rate: probability of crossover between two parents
        - elitism: number of best individuals to preserve in each generation
        """
        self.items = items
        self.weights = weights
        self.values = values
        self.max_weight = max_weight
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism = elitism
        self.num_items = len(items)
        
        # Metrics to track
        self.best_fitness_history = []
        self.avg_fitness_history = []
        
    def generate_individual(self):
        """Generate a random individual (binary string)"""
        return [random.randint(0, 1) for _ in range(self.num_items)]
    
    def initialize_population(self):
        """Initialize a random population"""
        return [self.generate_individual() for _ in range(self.population_size)]
    
    def calculate_fitness(self, individual):
        """
        Calculate the fitness of an individual
        
        Fitness is the total value if weight constraint is satisfied, 
        otherwise it's penalized
        """
        total_weight = sum(w * gene for w, gene in zip(self.weights, individual))
        total_value = sum(v * gene for v, gene in zip(self.values, individual))
        
        # Apply penalty if weight exceeds capacity
        if total_weight > self.max_weight:
            return 0  # Invalid solution
        
        return total_value
    
    def select_parent(self, population, fitnesses):
        """
        Select parent using tournament selection
        """
        # Tournament selection with tournament size of 3
        tournament_size = 3
        tournament_indices = random.sample(range(len(population)), tournament_size)
        tournament_fitnesses = [fitnesses[i] for i in tournament_indices]
        winner_idx = tournament_indices[tournament_fitnesses.index(max(tournament_fitnesses))]
        return population[winner_idx]
    
    def crossover(self, parent1, parent2):
        """
        Perform crossover between two parents to create two children
        Using single-point crossover
        """
        if random.random() < self.crossover_rate:
            crossover_point = random.randint(1, self.num_items - 1)
            child1 = parent1[:crossover_point] + parent2[crossover_point:]
            child2 = parent2[:crossover_point] + parent1[crossover_point:]
            return child1, child2
        return parent1[:], parent2[:]  # Return copies of parents
    
    def mutate(self, individual):
        """
        Apply mutation to an individual
        Flip bits with probability equal to mutation_rate
        """
        for i in range(self.num_items):
            if random.random() < self.mutation_rate:
                individual[i] = 1 - individual[i]  # Flip the bit (0->1 or 1->0)
        return individual
    
    def evolve(self):
        """Run the genetic algorithm"""
        start_time = time.time()
        population = self.initialize_population()
        
        for generation in range(self.generations):
            # Evaluate fitness for each individual
            fitnesses = [self.calculate_fitness(ind) for ind in population]
            
            # Track metrics
            best_fitness = max(fitnesses)
            avg_fitness = sum(fitnesses) / len(fitnesses)
            self.best_fitness_history.append(best_fitness)
            self.avg_fitness_history.append(avg_fitness)
            
            # Create new generation
            new_population = []
            
            # Elitism: keep the best individuals
            elite_indices = sorted(range(len(fitnesses)), key=lambda i: fitnesses[i], reverse=True)[:self.elitism]
            for idx in elite_indices:
                new_population.append(population[idx][:])  # Add a copy of the elite individual
            
            # Create rest of new population
            while len(new_population) < self.population_size:
                # Selection
                parent1 = self.select_parent(population, fitnesses)
                parent2 = self.select_parent(population, fitnesses)
                
                # Crossover
                child1, child2 = self.crossover(parent1, parent2)
                
                # Mutation
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                
                # Add to new population
                new_population.append(child1)
                if len(new_population) < self.population_size:
                    new_population.append(child2)
            
            # Replace old population with new population
            population = new_population
            
            if generation % 20 == 0:
                elapsed = time.time() - start_time
                print(f"Generation {generation}/{self.generations} ({elapsed:.2f}s): Best Fitness = {best_fitness}, Avg Fitness = {avg_fitness:.2f}")
        
        # Return best solution from final population
        final_fitnesses = [self.calculate_fitness(ind) for ind in population]
        best_idx = final_fitnesses.index(max(final_fitnesses))
        best_solution = population[best_idx]
        
        total_time = time.time() - start_time
        print(f"\nTotal runtime: {total_time:.2f} seconds")
        
        return best_solution, max(final_fitnesses)
    
    def display_solution(self, solution):
        """Display the items selected in the best solution"""
        total_value = 0
        total_weight = 0
        
        print("\nBest Solution:")
        print("Item\tWeight\tValue\tIncluded")
        print("-" * 35)
        
        included_items = []
        for i, (item, weight, value) in enumerate(zip(self.items, self.weights, self.values)):
            if solution[i] == 1:
                included = "Yes"
                included_items.append((item, weight, value))
                total_value += value
                total_weight += weight
            else:
                included = "No"
                
            # Only print if included to avoid overwhelming output for large problems
            if solution[i] == 1:
                print(f"{item}\t{weight}\t{value}\t{included}")
                
        print("-" * 35)
        print(f"Total Items: {len(included_items)}/{self.num_items}")
        print(f"Total Weight: {total_weight}/{self.max_weight}")
        print(f"Total Value: {total_value}")
    
    def plot_progress(self):
        """Plot the progress of the genetic algorithm"""
        plt.figure(figsize=(12, 6))
        plt.plot(self.best_fitness_history, label='Best Fitness')
        plt.plot(self.avg_fitness_history, label='Average Fitness')
        plt.xlabel('Generation')
        plt.ylabel('Fitness (Value)')
        plt.title('Genetic Algorithm Progress')
        plt.legend()
        plt.grid(True)
        plt.show()


# Example usage with a much larger problem
if __name__ == "__main__":
    # Create a large problem with 100 items
    num_items =100
    
    # Generate random item names
    categories = ["Electronics", "Books", "Tools", "Food", "Clothing", "Medicine", "Jewelry", "Supplies"]
    items = []
    for i in range(num_items):
        category = random.choice(categories)
        items.append(f"{category}_{i+1}")
    
    # Generate weights between 0.1 and 10.0
    weights = [round(random.uniform(0.1, 10.0), 1) for _ in range(num_items)]
    
    # Generate values between 10 and 1000, with some correlation to weight
    values = []
    for w in weights:
        # Base value proportional to weight with some randomness
        base_value = w * random.uniform(20, 100)
        # Add random variation
        value = int(base_value + random.uniform(-100, 500))
        # Ensure minimum value of 10
        values.append(max(10, value))
    
    # Set max weight to about 25-30% of total weight
    total_weight = sum(weights)
    max_weight = total_weight * random.uniform(0.25, 0.3)
    
    print(f"Problem size: {num_items} items")
    print(f"Total weight of all items: {total_weight:.1f}")
    print(f"Knapsack capacity: {max_weight:.1f}")
    
    # Initialize and run the genetic algorithm with increased parameters
    ga = KnapsackGA(
        items=items,
        weights=weights,
        values=values,
        max_weight=max_weight,
        population_size=500,   # Larger population
        generations=400, #1000,      # More generations
        mutation_rate=0.05,    # Lower mutation rate for stability
        crossover_rate=0.85,   # Higher crossover rate
        elitism=5              # More elites preserved
    )
    
    print("\nStarting genetic algorithm optimization...")
    best_solution, best_fitness = ga.evolve()
    ga.display_solution(best_solution)
    ga.plot_progress()
    
    # Compute how close we are to optimal (if we knew it)
    # For larger problems, the optimal solution is unknown, but we can estimate
    # the quality of our solution in other ways
    
    # 1. Density ratio (value per weight unit)
    item_densities = [(v/w, i) for i, (w, v) in enumerate(zip(weights, values))]
    item_densities.sort(reverse=True)  # Sort by density (highest first)
    
    # 2. Greedy solution (for comparison)
    greedy_selection = [0] * num_items
    greedy_weight = 0
    greedy_value = 0
    
    for density, idx in item_densities:
        if greedy_weight + weights[idx] <= max_weight:
            greedy_selection[idx] = 1
            greedy_weight += weights[idx]
            greedy_value += values[idx]
    
    print("\nComparison with greedy approach:")
    print(f"Greedy solution value: {greedy_value}")
    print(f"Genetic algorithm solution value: {best_fitness}")
    print(f"Improvement: {((best_fitness - greedy_value) / greedy_value * 100):.2f}%")