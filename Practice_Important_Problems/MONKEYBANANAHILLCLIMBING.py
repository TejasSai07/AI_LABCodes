def manhattan_distance(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])
    
def find_neighbors(maze, current, end):
    x, y = current
    neighbors = []
    
    if x > 0 and maze[x - 1][y] != 1:
        neighbors.append(((x - 1, y), manhattan_distance((x - 1, y), end)))
    if x < 4 and maze[x + 1][y] != 1:
        neighbors.append(((x + 1, y), manhattan_distance((x + 1, y), end)))
    if y > 0 and maze[x][y - 1] != 1:
        neighbors.append(((x, y - 1), manhattan_distance((x, y - 1), end)))
    if y < 4 and maze[x][y + 1] != 1:
        neighbors.append(((x, y + 1), manhattan_distance((x, y + 1), end)))
    
    return neighbors

def steepest_hillclimbing(maze, start, end):
    current = start
    steps = 0
    
    while current != end:
        neighbors = find_neighbors(maze, current, end)
        best_neighbor, best_cost = min(neighbors, key=lambda x: x[1])
        
        print(neighbors, best_neighbor)
        
        """
        if best_cost <= steps:  # If the best cost doesn't decrease, exit
            break
        """
        if best_cost >= manhattan_distance(current, end):
            break
        
        current = best_neighbor
        steps += 1
    
    print("Number of steps taken:", steps)

maze = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

steepest_hillclimbing(maze, start, end)
