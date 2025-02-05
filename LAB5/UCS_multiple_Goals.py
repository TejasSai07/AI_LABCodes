graph = {
    'S': {'A': 5, 'B': 3, 'C': 2},
    'A': {'G1': 4},
    'B': {'G2': 7},
    'C': {'G3': 6},
    'G1': {},
    'G2': {},
    'G3': {}
}

def ucs(graph, start):
    frontier = [(0, start)]  
    visited = set()  
    came_from = {}  
    cost_so_far = {start: 0}  

    while frontier:
        priority, current = min(frontier)  
        frontier.remove((priority, current))
        visited.add(current)

        if current.startswith('G'):
            return current, cost_so_far[current] 

        for next_node, cost in graph[current].items():
            new_cost = cost_so_far[current] + cost
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                came_from[next_node] = current
                if next_node not in visited:
                    frontier.append((new_cost, next_node))

    return None, None  

start_node = 'S'
goal_node, cumulative_cost = ucs(graph, start_node)
print("Goal node with the least cumulative cost from", start_node, ":", goal_node, "with cost", cumulative_cost)
