import random

class TomatoGeneticAlgorithm:
    def __init__(self, pop_size=10, mutation_rate=0.1, generations=20):
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate
        self.generations = generations
        # Each gene represents: [Size (1-9), Color (1-9), Sweetness (1-9)]
        self.gene_min = 1
        self.gene_max = 9
        self.chromosome_length = 3

    def create_individual(self):
        """Generates a random chromosome representing a tomato plant: [Size, Color, Sweetness]"""
        return [random.randint(self.gene_min, self.gene_max) for _ in range(self.chromosome_length)]

    def initialize_population(self):
        """Initializes the population of tomato plants."""
        return [self.create_individual() for _ in range(self.pop_size)]

    def calculate_fitness(self, chromosome):
        """Fitness is the sum of the traits: higher is better (Target: [9, 9, 9] -> Fitness 27)"""
        return sum(chromosome)

    def select_parents(self, population, fitness_scores):
        """Selects parents using Roulette Wheel Selection (fitness proportionate selection)."""
        total_fitness = sum(fitness_scores)
        if total_fitness == 0:
            return random.choice(population), random.choice(population)
        
        def draw_one():
            pick = random.uniform(0, total_fitness)
            current = 0
            for ind, fit in zip(population, fitness_scores):
                current += fit
                if current > pick:
                    return ind
            return population[-1]

        return draw_one(), draw_one()

    def crossover(self, parent1, parent2):
        """Performs single-point crossover to generate two offspring."""
        crossover_point = random.randint(1, self.chromosome_length - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    def mutate(self, chromosome):
        """Mutates a gene with a given mutation probability to maintain diversity."""
        mutated_chromosome = chromosome.copy()
        for idx in range(self.chromosome_length):
            if random.random() < self.mutation_rate:
                # Randomly change the gene value to a new value between 1 and 9
                mutated_chromosome[idx] = random.randint(self.gene_min, self.gene_max)
        return mutated_chromosome

    def run(self):
        """Runs the complete Genetic Algorithm simulation."""
        population = self.initialize_population()
        print(f"Initial Population: {population}\n")

        for gen in range(1, self.generations + 1):
            fitness_scores = [self.calculate_fitness(ind) for ind in population]
            
            # Find the best individual of the current generation
            best_fit = max(fitness_scores)
            best_ind = population[fitness_scores.index(best_fit)]
            
            print(f"Gen {gen:02d} | Best Fitness: {best_fit} | Best Chromosome: {best_ind} | Avg Fitness: {sum(fitness_scores)/self.pop_size:.2f}")
            
            # Check if optimal tomato plant [9, 9, 9] is found
            if best_fit == 27:
                print(f"\n🎉 Perfect Tomato Plant [9, 9, 9] found in Generation {gen}!")
                break

            # Create next generation
            next_generation = []
            while len(next_generation) < self.pop_size:
                p1, p2 = self.select_parents(population, fitness_scores)
                c1, c2 = self.crossover(p1, p2)
                next_generation.append(self.mutate(c1))
                if len(next_generation) < self.pop_size:
                    next_generation.append(self.mutate(c2))
            
            population = next_generation

if __name__ == "__main__":
    # Seed for reproducibility
    random.seed(42)
    ga = TomatoGeneticAlgorithm(pop_size=8, mutation_rate=0.15, generations=15)
    ga.run()
