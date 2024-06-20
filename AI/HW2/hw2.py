import random
import math


distance_matrix = [
    [0, 2, 9, 10, 7],
    [2, 0, 8, 5, 6],
    [9, 8, 0, 3, 4],
    [10, 5, 3, 0, 2],
    [7, 6, 4, 2, 0]
]

def total_distance(path, distance_matrix):
   
    distance = 0
    for i in range(len(path) - 1):
        distance += distance_matrix[path[i]][path[i + 1]]
    distance += distance_matrix[path[-1]][path[0]] 
    return distance

def get_neighbor(path):
   
    new_path = path[:]
    i, j = random.sample(range(len(path)), 2)
    new_path[i], new_path[j] = new_path[j], new_path[i]
    return new_path

def hill_climbing(distance_matrix, iterations=1000):
  
    n = len(distance_matrix)
    current_path = list(range(n))
    random.shuffle(current_path)
    current_distance = total_distance(current_path, distance_matrix)

    for _ in range(iterations):
        neighbor_path = get_neighbor(current_path)
        neighbor_distance = total_distance(neighbor_path, distance_matrix)
        
        if neighbor_distance < current_distance:
            current_path = neighbor_path
            current_distance = neighbor_distance
    
    return current_path, current_distance


best_path, best_distance = hill_climbing(distance_matrix)
print(f"bestpath: {best_path}")
print(f"bestdistance: {best_distance}")
