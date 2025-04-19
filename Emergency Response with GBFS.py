import heapq
import time

# ---------------------- GRID & HEURISTIC ----------------------
grid = [
    ['S', '.', 'T', '.', '.'],
    ['.', 'T', '.', '.', '.'],
    ['.', '.', '.', 'T', 'H']
]

rows, cols = len(grid), len(grid[0])

def find_pos(symbol):
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == symbol:
                return (r, c)

start = find_pos('S')
goal = find_pos('H')

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# ---------------------- GBFS ----------------------
def gbfs_grid(start, goal):
    open_set = [(manhattan(start, goal), start)]
    came_from = {}
    visited = set()
    nodes_explored = 0

    while open_set:
        _, current = heapq.heappop(open_set)
        nodes_explored += 1
        if current == goal:
            break
        visited.add(current)
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = current[0]+dr, current[1]+dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr,nc) not in visited and grid[nr][nc] != 'T':
                    came_from[(nr,nc)] = current
                    heapq.heappush(open_set, (manhattan((nr,nc), goal), (nr,nc)))
    return reconstruct(came_from, start, goal), nodes_explored

def reconstruct(came_from, start, goal):
    path = [goal]
    current = goal
    while current != start:
        current = came_from.get(current)
        if current is None: return []
        path.append(current)
    path.reverse()
    return path

# ---------------------- RUN ----------------------
start_time = time.time()
path, nodes = gbfs_grid(start, goal)
elapsed = (time.time() - start_time) * 1000

# Visualisasi Grid
visual_grid = [row[:] for row in grid]
for r, c in path:
    if visual_grid[r][c] not in ('S', 'H'):
        visual_grid[r][c] = '*'

print("\nComparing result (based on Time in millisecond)")
print("Assignment\tGBFS\t\tA star")
print(f"2\t\t{elapsed:.2f} ms\t0.00 ms")  # ← A* dummy

print("\nComparing result (based on number of nodes)")
print("Assignment\tGBFS\tA star")
print(f"2\t\t{nodes}\t0")  # ← A* dummy

