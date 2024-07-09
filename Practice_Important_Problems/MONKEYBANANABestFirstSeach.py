def manhattan_distance(new, goal) :
    return abs(new[0] - goal[0]) + abs(new[1] - goal[1])
    

def find_neighbors(maze,start) :
    x,y = start
    neighbors = []
    
    if (x > 0) :
        dx, dy = (x - 1 , y)
        if maze[dx][dy] != 1 : 
            neighbors.append((dx,dy))
    if (x < 4) :
        dx, dy = (x + 1 , y)
        if maze[dx][dy] != 1 : 
            neighbors.append((dx,dy))
    if (y > 0) :
        dx, dy = (x , y-1)
        if maze[dx][dy] != 1 : 
            neighbors.append((dx,dy))
    if (y < 4) :
        dx, dy = (x , y+1)
        if maze[dx][dy] != 1 : 
            neighbors.append((dx,dy))
    
    return neighbors

def bestfirstsearch(maze, start, end):
    current = start
    steps = 0
    path = [current]
    
    while current != end:
        neighbors = find_neighbors(maze, current)
        min_cost = float('inf')
        next_node = None
        
        for neigh in neighbors:
            new_cost = manhattan_distance(neigh, end)
            if new_cost < min_cost:
                min_cost = new_cost
                next_node = neigh
        
        if next_node is None:
            # No reachable neighbors
            break
        
        current = next_node
        path.append(current)
        steps += 1
        
    print("Path:", path)
    print("Total steps:", steps)

maze = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

bestfirstsearch(maze, start, end)
