
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
    

def astar(maze,start,end) :
    frontier = [(0,start)]
    cost_so_far = {start : 0}
    came_from = {}
    
    
    while frontier : 
        _,curr = min(frontier)
        
    
        if curr == end :
            break
        
        frontier.remove((_,curr))
        
        for next_node in find_neighbors(maze,curr) : 
            new_cost = cost_so_far[curr] + 1
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node] :
                cost_so_far[next_node] = new_cost
                priority = new_cost + manhattan_distance(next_node,end)
                frontier.append((priority,next_node))
                came_from[next_node] = curr
    path = []
    current = end
    while current != start:
        path.append((current))
        current = came_from[current]
    path.append(start)
    path.reverse()

    return path,cost_so_far[end]


maze = [[0,1,0,0,0],
        [0,0,1,1,0],
        [0,0,0,0,1],
        [1,0,0,1,0],
        [1,0,0,0,0]]
        
start = (0,0)
end = (4,4)

shortest_path,cost = astar(maze, start, end)
print("Shortest path:", shortest_path)
print("Cost is : ",cost)
