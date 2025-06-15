import heapq

# Goal configuration
GOAL = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

# Directions: move offset in the flat list
DIRECTIONS = {
    'U': -3,
    'D': 3,
    'L': -1,
    'R': 1
}

# Valid move constraints
def is_valid_move(pos, move):
    if move == 'U' and pos < 3: return False
    if move == 'D' and pos > 5: return False
    if move == 'L' and pos % 3 == 0: return False
    if move == 'R' and pos % 3 == 2: return False
    return True

# Heuristic: Manhattan distance
def manhattan(board):
    dist = 0
    for i, val in enumerate(board):
        if val != 0:
            goal_i = GOAL.index(val)
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_i, 3)
            dist += abs(x1 - x2) + abs(y1 - y2)
    return dist

# Move function
def move(board, direction, blank):
    new_board = board[:]
    delta = DIRECTIONS[direction]
    new_blank = blank + delta
    new_board[blank], new_board[new_blank] = new_board[new_blank], new_board[blank]
    return new_board, new_blank

# A* Search
def a_star(start):
    start_h = manhattan(start)
    start_state = (start_h, 0, start, start.index(0), [])  # (f, g, board, blank_pos, path)
    
    heap = [start_state]
    visited = set()

    while heap:
        f, g, board, blank, path = heapq.heappop(heap)

        if board == GOAL:
            return path + [board]

        visited.add(tuple(board))

        for direction in DIRECTIONS:
            if not is_valid_move(blank, direction):
                continue

            new_board, new_blank = move(board, direction, blank)
            if tuple(new_board) in visited:
                continue

            h = manhattan(new_board)
            heapq.heappush(heap, (g + 1 + h, g + 1, new_board, new_blank, path + [board]))

    return None

# Print board
def print_board(board):
    for i in range(0, 9, 3):
        row = board[i:i+3]
        print(' '.join(str(x) if x != 0 else ' ' for x in row))
    print()

# Run
initial = [1, 2, 3,
           4, 0, 5,
           6, 7, 8]

solution = a_star(initial)

if solution:
    print("Solution found! Steps:")
    for step, board in enumerate(solution):
        print(f"Step {step}:")
        print_board(board)
    print("Final Goal State:")
    print_board(GOAL)
else:
    print("No solution found.")
