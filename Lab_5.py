import heapq

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def means_end_analysis(grid_size, start, goal):
    m, n = grid_size
    visited = set()
    pq = []  # priority queue: (heuristic, current_position, path)
    
    h_start = manhattan_distance(start, goal)
    heapq.heappush(pq, (h_start, start, [start]))
    directions = [(0,1), (1,0), (0,-1), (-1,0)] 
    while pq:
        h, current, path = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path

        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < m and 0 <= ny < n:
                neighbor = (nx, ny)
                if neighbor not in visited:
                    h_next = manhattan_distance(neighbor, goal)
                    heapq.heappush(pq, (h_next, neighbor, path + [neighbor]))
    return None  

grid_size = (5, 5)
start = (0, 0)
goal = (4, 4)
path = means_end_analysis(grid_size, start, goal)

print("Path using heuristic-driven Means-End Analysis:")
for step in path:
    print(step)
