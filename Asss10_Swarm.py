import numpy as np


# Function to calculate distance between two cities
def distance(city1, city2):
    return np.linalg.norm(city1 - city2)


# Function to initialize pheromone trails
def init_pheromone(num_cities):
    return np.ones((num_cities, num_cities))


# Function to update pheromone trails
def update_pheromone(pheromone, delta_pheromone, rho):
    return (1 - rho) * pheromone + delta_pheromone


# Function to perform ant movement
def ant_movement(num_ants, pheromone, distances, alpha, beta):
    num_cities = len(distances)
    paths = []
    for ant in range(num_ants):
        path = []
        visited = set()
        current_city = np.random.randint(num_cities)
        visited.add(current_city)
        path.append(current_city)
        while len(visited) < num_cities:
            probabilities = []
            for city in range(num_cities):
                if city not in visited:
                    pheromone_factor = pheromone[current_city][city] ** alpha
                    distance_factor = (1.0 / distances[current_city][city]) ** beta
                    probabilities.append((city, pheromone_factor * distance_factor))
            probabilities = np.array(probabilities)
            probabilities[:, 1] /= np.sum(probabilities[:, 1])
            next_city = np.random.choice(probabilities[:, 0], p=probabilities[:, 1])
            visited.add(next_city)
            path.append(int(next_city))
            current_city = int(next_city)
        paths.append(path)
    return paths


# Function to calculate total distance of a path
def total_distance(path, distances):
    total = 0
    num_cities = len(path)
    for i in range(num_cities - 1):
        total += distances[path[i]][path[i + 1]]
    total += distances[path[-1]][path[0]]
    return total


# Function to evaporate pheromone trails
def evaporate_pheromone(pheromone, evaporation_rate):
    return (1 - evaporation_rate) * pheromone


# Function to solve TSP using Ant Colony Optimization
def solve_tsp(num_cities, num_ants, iterations, alpha, beta, rho, evaporation_rate):
    cities = np.random.rand(num_cities, 2)  # Generate random cities
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = distance(cities[i], cities[j])
            distances[i][j] = dist
            distances[j][i] = dist

    pheromone = init_pheromone(num_cities)
    best_distance = float("inf")
    best_path = None

    for _ in range(iterations):
        paths = ant_movement(num_ants, pheromone, distances, alpha, beta)
        for path in paths:
            path_distance = total_distance(path, distances)
            if path_distance < best_distance:
                best_distance = path_distance
                best_path = path
        delta_pheromone = np.zeros((num_cities, num_cities))
        for path in paths:
            for i in range(num_cities - 1):
                delta_pheromone[path[i]][path[i + 1]] += 1 / total_distance(
                    path, distances
                )
            delta_pheromone[path[-1]][path[0]] += 1 / total_distance(path, distances)
        pheromone = update_pheromone(pheromone, delta_pheromone, rho)
        pheromone = evaporate_pheromone(pheromone, evaporation_rate)

    return best_distance, best_path


# Example usage
num_cities = 20
num_ants = 10
iterations = 100
alpha = 1.0
beta = 2.0
rho = 0.1
evaporation_rate = 0.1

best_distance, best_path = solve_tsp(
    num_cities, num_ants, iterations, alpha, beta, rho, evaporation_rate
)
print(f"Shortest distance: {best_distance}")
print(f"Best path: {best_path}")













import numpy as np
import random

def distance(city1, city2):
    return np.linalg.norm(city1 - city2) 

num_cities = 4
num_ants = 4
evaporation_rate = 0.05
alpha = 1
beta = 1

cities = np.random.rand(num_cities, 2)
# cities = [[1,2], [3,4], [5,6], [7,8]]

distances = []
# distances = [[0, 2, 3, 4],      #0
#              [2, 0, 3, 4],      #1
#              [3, 1, 0, 4],      #2
#              [1, 2, 3, 0]]      #3
for city1 in cities:
    temp = []
    for city2 in cities: 
        temp.append(distance(city1, city2))
    distances.append(temp)

phermones = np.random.rand(num_cities, num_cities)
# phermones = [[0, 2, 3, 4],
#              [2, 0, 3, 4],
#              [3, 1, 0, 4],
#              [1, 2, 3, 0]]

tour_lengths = []
tour_paths = []

for _ in range(num_ants):
    randomly_selected_city = random.randint(0, num_cities-1)
    selected_city = randomly_selected_city
    tour_length = 0
    tour_path = []
    for j in range(num_cities): 
        tour_path.append(selected_city)
        dist = distances[selected_city]
        phero = phermones[selected_city]
        stochastic_gradient_descent = []
        for i in range(len(dist)):
            if dist[i] != 0: stochastic_gradient_descent.append(((phero[i])**alpha)*((1/dist[i])**beta))
            else: stochastic_gradient_descent.append(0)
        
        total_eta = sum(stochastic_gradient_descent)
        for i in range(len(stochastic_gradient_descent)):
            stochastic_gradient_descent[i]= stochastic_gradient_descent[i] / total_eta
        
        # eta = [1, 2, 3, 4] solution_set = [1, 3, 6, 10]
        solution_set, temp = [], 0
        for i in range(len(stochastic_gradient_descent)):
            temp += stochastic_gradient_descent[i]
            solution_set.append(temp)

        random_value = random.random()    # 0 to 1
        for i in range(len(solution_set)): 
            if random_value <= solution_set[i]:
                if i not in tour_path:
                    selected_city = i
                    break
        tour_length += dist[selected_city]

        for i in range(len(phero)): 
            phero[i] = (1 - evaporation_rate)*phero[i]
        phermones[selected_city] = phero
        
    tour_length += distances[randomly_selected_city][selected_city]
    tour_path.append(randomly_selected_city)   

    tour_lengths.append(tour_length)
    tour_paths.append(tour_path)

minimum_index = tour_lengths.index(min(tour_lengths))
print("Shortest Distance: ", tour_lengths[minimum_index])
print("Shortest Path: ",  tour_paths[minimum_index])
