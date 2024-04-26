import random
from deap import creator, base, tools, algorithms

creator.create("FitnessMax", base.Fitness, weights=(1.0,))   
# it creates fitnessmax class by using base.fitness inbuilt class from deap with fitness maximization approach

creator.create("Individual", list, fitness=creator.FitnessMax) 
#creates individual class having maximum fitness



toolbox = base.Toolbox()



#set up the DEAP toolbox with the necessary functions for creating individuals and populations for the genetic algorithm

toolbox.register("attr_bool", random.randint, 0, 1) 
#registers function attr_bool in deap that generates attribute for individuals in population here this lies between 0 and 1

toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=100)  
#it cretes a function individual for creating individuals by repeating attr_bool function for 100 times to save 100 binary attributes with each individual

toolbox.register("population", tools.initRepeat, list, toolbox.individual)
#creates entire population having multiple individuals and repeated individual function to add new individual


#takes an individual (candidate solution) as input.
def evalOneMax(individual):
    return sum(individual),          #sum of the binary values in the individualand cretes a tuple with single elment



toolbox.register("evaluate", evalOneMax)  
#registers evalonemax function on deap as evaluate to calculate  fitness of individual

toolbox.register("mate", tools.cxTwoPoint)      
#registers the tools.cxTwoPoint function as the crossover operator in the DEAP toolbox
#The crossover operator is responsible for combining genetic information from two parent individuals to produce offspring individuals. 
#In this case, tools.cxTwoPoint performs a two-point crossover

toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
# mutation operator: responsible for introducing random changes to the genetic information of individuals to maintain diversity 
#in the population. tools.mutFlipBit flips bits in the individual with a probability of 0.05 (indpb=0.05).

toolbox.register("select", tools.selTournament, tournsize=3)
#selection operator: The selection operator is responsible for selecting individuals from the population 
#to undergo genetic operations (crossover and mutation) to form the next generation. 
#In this case, tools.selTournament performs tournament selection with a tournament size of 3 (tournsize=3).

population = toolbox.population(n=300)

NGEN=40
for gen in range(NGEN):
    
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
    #generates offspring by applying variation operators (crossover and mutation) to the current population (population). 
    #It uses the varAnd function from the algorithms module, which performs crossover (cxpb=0.5, crossover probability) 
    #and mutation (mutpb=0.1, mutation probability) with a certain probability for each.
    
    fits = toolbox.map(toolbox.evaluate, offspring)
    #evaluates the fitness of each offspring in the population using the evaluation function (toolbox.evaluate). 
    #It uses the map function to efficiently apply the evaluation function to each offspring in parallel.
    
    for fit, ind in zip(fits, offspring): #assigns the calculated fitness values to the corresponding offspring individuals.
        ind.fitness.values = fit   
    population = toolbox.select(offspring, k=len(population))
    #selects individuals from the offspring population to form the next generation of the population. 
        #It uses the selection operator (toolbox.select) to select individuals based on their fitness values.
        
top10 = tools.selBest(population, k=10) #selects the top 10 individuals from the final population using the tools.selBest function. 
                                         #It returns a list of the top individuals.
    
    
print(len(top10[0]))
