class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))

def dfs_water_jug_problem(capacity1, capacity2, target):
    start_state = State(0, 0)
    visited = set()

    def dfs(state):
        if state == target:
            return state

        visited.add(state)

        next_states = [
            State(capacity1, state.jug2),  
            State(state.jug1, capacity2),  
            State(0, state.jug2),          
            State(state.jug1, 0),         
            State(max(0, state.jug1 - (capacity2 - state.jug2)), 
                  min(capacity2, state.jug1 + state.jug2)), 
            State(min(capacity1, state.jug1 + state.jug2),
                  max(0, state.jug2 - (capacity1 - state.jug1)))  
        ]

        for next_state in next_states:
            if next_state not in visited:
                result = dfs(next_state)
                if result:
                    return result

        return None

    return dfs(start_state)

def get_user_input():
    capacity_jug1 = int(input("Enter capacity of jug 1: "))
    capacity_jug2 = int(input("Enter capacity of jug 2: "))
    target_jug1 = int(input("Enter desired amount of water in jug 1: "))
    target_jug2 = int(input("Enter desired amount of water in jug 2: "))
    return capacity_jug1, capacity_jug2, State(target_jug1, target_jug2)

capacity_jug1, capacity_jug2, target_state = get_user_input()

result = dfs_water_jug_problem(capacity_jug1, capacity_jug2, target_state)
if result:
    print(f"Target state ({target_state.jug1}, {target_state.jug2}) is reachable.")
else:
    print("Target state is not reachable.")
