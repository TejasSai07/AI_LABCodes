# Define the 5x5 matrix
matrix = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]

# Define the initial and goal states
initial_state = (0, 0)
goal_state = (4, 3)

def steepest_hill_climbing(matrix, initial_state, goal_state):
    current_state = initial_state
    path_cost = 0
    
    while current_state != goal_state:
        neighbors = []
        x, y = current_state
        
        # Generate neighboring states
        if x > 0 and matrix[x - 1][y] != 1:
            neighbors.append((x - 1, y))
        if x < 4 and matrix[x + 1][y] != 1:
            neighbors.append((x + 1, y))
        if y > 0 and matrix[x][y - 1] != 1:
            neighbors.append((x, y - 1))
        if y < 4 and matrix[x][y + 1] != 1:
            neighbors.append((x, y + 1))
        
        # Choose the neighbor with minimum distance to the goal
        min_distance = float('inf')
        next_state = None
        for neighbor in neighbors:
            distance = abs(neighbor[0] - goal_state[0]) + abs(neighbor[1] - goal_state[1])
            if distance < min_distance:
                min_distance = distance
                next_state = neighbor
        
        # Move to the next state
        current_state = next_state
        path_cost += 1
    
    return path_cost

def uniform_cost_search(matrix, initial_state, goal_state):
    frontier = [(0, initial_state)]
    explored = set()
    
    while frontier:
        cost, current_state = frontier.pop(0)
        
        if current_state == goal_state:
            return cost
        
        explored.add(current_state)
        
        x, y = current_state
        
        # Generate neighboring states
        neighbors = []
        if x > 0 and matrix[x - 1][y] != 1:
            neighbors.append((x - 1, y))
        if x < 4 and matrix[x + 1][y] != 1:
            neighbors.append((x + 1, y))
        if y > 0 and matrix[x][y - 1] != 1:
            neighbors.append((x, y - 1))
        if y < 4 and matrix[x][y + 1] != 1:
            neighbors.append((x, y + 1))
        
        # Add neighbors to the frontier with their costs
        for neighbor in neighbors:
            if neighbor not in explored:
                new_cost = cost + 1
                frontier.append((new_cost, neighbor))
                frontier.sort()  # Sort the frontier based on cost
    
    return None  # If goal state is not reachable

# Calculate path cost using steepest hill climbing
steepest_cost = steepest_hill_climbing(matrix, initial_state, goal_state)
print("Path cost using steepest hill climbing:", steepest_cost)

# Calculate path cost using UCS
ucs_cost = uniform_cost_search(matrix, initial_state, goal_state)
print("Path cost using UCS:", ucs_cost)
