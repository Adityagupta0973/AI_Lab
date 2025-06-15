import math
import heapq

class Cell:
    def __init__(self):
        self.parent_i = 0
        self.parent_j = 0
        self.f = float('inf')
        self.g = float('inf')
        self.h = 0

ROW, COL = 9, 10

def is_valid(row, col):
    return 0 <= row < ROW and 0 <= col < COL

def is_unblocked(grid, row, col):
    return grid[row][col] == 1

def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]

def calculate_h_value(row, col, dest):
    return math.hypot(row - dest[0], col - dest[1])

def trace_path(cell_details, dest):
    path = []
    row, col = dest
    while (cell_details[row][col].parent_i, cell_details[row][col].parent_j) != (row, col):
        path.append((row, col))
        row, col = cell_details[row][col].parent_i, cell_details[row][col].parent_j
    path.append((row, col))
    path.reverse()
    
    print("The Path is:")
    for pos in path:
        print("->", pos, end=" ")
    print()

def a_star_search(grid, src, dest):
    if not is_valid(*src) or not is_valid(*dest):
        print("Source or destination is invalid")
        return
    if not is_unblocked(grid, *src) or not is_unblocked(grid, *dest):
        print("Source or destination is blocked")
        return
    if src == dest:
        print("Already at the destination")
        return

    closed_list = [[False] * COL for _ in range(ROW)]
    cell_details = [[Cell() for _ in range(COL)] for _ in range(ROW)]

    si, sj = src
    cell_details[si][sj].f = cell_details[si][sj].g = cell_details[si][sj].h = 0
    cell_details[si][sj].parent_i, cell_details[si][sj].parent_j = si, sj

    open_list = [(0.0, si, sj)]

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    while open_list:
        f, i, j = heapq.heappop(open_list)
        closed_list[i][j] = True

        for d in directions:
            ni, nj = i + d[0], j + d[1]

            if is_valid(ni, nj) and is_unblocked(grid, ni, nj) and not closed_list[ni][nj]:
                if is_destination(ni, nj, dest):
                    cell_details[ni][nj].parent_i, cell_details[ni][nj].parent_j = i, j
                    print("The destination cell is found")
                    trace_path(cell_details, dest)
                    return

                g_new = cell_details[i][j].g + 1.0
                h_new = calculate_h_value(ni, nj, dest)
                f_new = g_new + h_new

                if cell_details[ni][nj].f > f_new:
                    cell_details[ni][nj].f = f_new
                    cell_details[ni][nj].g = g_new
                    cell_details[ni][nj].h = h_new
                    cell_details[ni][nj].parent_i, cell_details[ni][nj].parent_j = i, j
                    heapq.heappush(open_list, (f_new, ni, nj))

    print("Failed to find the destination cell")

grid = [
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
]

src = [0, 0]
dest = [8, 0]
a_star_search(grid, src, dest)