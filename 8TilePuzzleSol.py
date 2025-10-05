import random
from collections import deque

# ----------------------------
# Utility Functions
# ----------------------------

# Goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  # 0 represents blank

goal_tuple = tuple(sum(goal_state, []))  # Flattened

# Moves: Up, Down, Left, Right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
move_names = ["Up", "Down", "Left", "Right"]


def is_solvable(state):
    """Check if puzzle state is solvable using inversion parity."""
    flat = [n for n in sum(state, []) if n != 0]
    inversions = sum(1 for i in range(len(flat)) for j in range(i + 1, len(flat)) if flat[i] > flat[j])
    return inversions % 2 == 0


def get_blank_pos(state):
    """Return (row, col) of blank (0)."""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def swap_and_create(state, i1, j1, i2, j2):
    """Return new state after swapping two positions."""
    new_state = [row[:] for row in state]
    new_state[i1][j1], new_state[i2][j2] = new_state[i2][j2], new_state[i1][j1]
    return new_state


def state_to_tuple(state):
    return tuple(sum(state, []))


def print_state(state):
    for row in state:
        print(row)
    print()


# ----------------------------
# Iterative Deepening Search (IDS)
# ----------------------------

def dls(state, depth, path, visited, nodes_expanded):
    """Depth Limited Search"""
    nodes_expanded[0] += 1
    if state_to_tuple(state) == goal_tuple:
        return path

    if depth == 0:
        return None

    blank_i, blank_j = get_blank_pos(state)

    for (dx, dy), move_name in zip(moves, move_names):
        new_i, new_j = blank_i + dx, blank_j + dy
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = swap_and_create(state, blank_i, blank_j, new_i, new_j)
            t_state = state_to_tuple(new_state)
            if t_state not in visited:
                visited.add(t_state)
                res = dls(new_state, depth - 1, path + [move_name], visited, nodes_expanded)
                if res:
                    return res
                visited.remove(t_state)
    return None


def iterative_deepening(start_state):
    depth = 0
    nodes_expanded = [0]
    while True:
        visited = {state_to_tuple(start_state)}
        res = dls(start_state, depth, [], visited, nodes_expanded)
        if res:
            return res, nodes_expanded[0]
        depth += 1


# ----------------------------
# Bonus Task: Bidirectional Search
# ----------------------------

def get_neighbors(state):
    neighbors = []
    blank_i, blank_j = get_blank_pos(state)
    for (dx, dy), move_name in zip(moves, move_names):
        new_i, new_j = blank_i + dx, blank_j + dy
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = swap_and_create(state, blank_i, blank_j, new_i, new_j)
            neighbors.append((new_state, move_name))
    return neighbors


def bidirectional_search(start_state):
    start_t = state_to_tuple(start_state)

    if start_t == goal_tuple:
        return [], 0

    frontier_start = deque([(start_t, [])])
    frontier_goal = deque([(goal_tuple, [])])

    visited_start = {start_t: []}
    visited_goal = {goal_tuple: []}

    nodes_expanded = 0
    inverse_move = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}

    while frontier_start and frontier_goal:
        # Expand from start
        curr_t, path = frontier_start.popleft()
        curr_state = [list(curr_t[i:i + 3]) for i in range(0, 9, 3)]
        nodes_expanded += 1

        for neighbor, move_name in get_neighbors(curr_state):
            t_neighbor = state_to_tuple(neighbor)
            if t_neighbor not in visited_start:
                visited_start[t_neighbor] = path + [move_name]
                frontier_start.append((t_neighbor, path + [move_name]))
                if t_neighbor in visited_goal:
                    goal_path = [inverse_move[m] for m in visited_goal[t_neighbor][::-1]]
                    return visited_start[t_neighbor] + goal_path, nodes_expanded

        # Expand from goal
        curr_t, path = frontier_goal.popleft()
        curr_state = [list(curr_t[i:i + 3]) for i in range(0, 9, 3)]
        nodes_expanded += 1

        for neighbor, move_name in get_neighbors(curr_state):
            t_neighbor = state_to_tuple(neighbor)
            if t_neighbor not in visited_goal:
                visited_goal[t_neighbor] = path + [move_name]
                frontier_goal.append((t_neighbor, path + [move_name]))
                if t_neighbor in visited_start:
                    goal_path = [inverse_move[m] for m in visited_goal[t_neighbor][::-1]]
                    return visited_start[t_neighbor] + goal_path, nodes_expanded

    return None, nodes_expanded


# ----------------------------
# Main Driver
# ----------------------------

if __name__ == "__main__":
    choice = input("Do you want to enter your own puzzle? (y/n): ").strip().lower()

    if choice == 'y':
        print("Enter your puzzle row by row (use 0 for the blank).")
        start_state = []
        for i in range(3):
            row = list(map(int, input(f"Row {i+1} (3 numbers separated by space): ").split()))
            start_state.append(row)
        if not is_solvable(start_state):
            print("The puzzle you entered is NOT solvable. Exiting.")
            exit(0)
    else:
        # Generate random solvable puzzle
        while True:
            nums = list(range(9))
            random.shuffle(nums)
            start_state = [nums[i:i + 3] for i in range(0, 9, 3)]
            if is_solvable(start_state):
                break

    print("Start State:")
    print_state(start_state)

    print("Goal State:")
    print_state(goal_state)

    if start_state==goal_state:
        print("Already in goal state .Exiting .")
        exit(0)

    # IDS
    print("----- Iterative Deepening Search -----")
    moves_seq, nodes = iterative_deepening(start_state)
    print("Moves:", moves_seq)
    print("Number of nodes expanded:", nodes)

    # Bidirectional
    print("\n----- Bidirectional Search (Bonus) -----")
    moves_seq, nodes = bidirectional_search(start_state)
    print("Moves:", moves_seq)
    print("Number of nodes expanded:", nodes)
