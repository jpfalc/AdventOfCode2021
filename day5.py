import numpy as np

# ---- Load Data ----
with open('data/day5.txt', 'rb') as f:
    clean_lines = (line.replace(b' -> ',b',') for line in f)
    data = np.genfromtxt(clean_lines, dtype=int, delimiter=',')
grid_size = 1000
danger_map = np.zeros(shape=(grid_size,grid_size), dtype=int)

# Applies a diagonal line to the grid
def apply_diag(line):
    x1, y1, x2, y2 = line[0], line[1], line[2], line[3]
    x_min, x_max = min(x1,x2), max(x1,x2)
    ind_rows, ind_cols = np.indices((grid_size,grid_size))
    empty = np.zeros(shape=(grid_size,grid_size), dtype=int)
    if ((x2 > x1) & (y2 > y1)) or ((x1 > x2) & (y1 > y2)): # positive slope
        top_x, top_y = min(x1,x2), min(y1,y2)
        empty[np.where((ind_rows - ind_cols == top_y - top_x) & (ind_cols >= x_min) & (ind_cols <= x_max))] = 1
    else: # negative slope
        top_x, top_y = max(x1,x2), min(y1,y2)
        empty[np.where((ind_rows + ind_cols == top_y + top_x) & (ind_cols >= x_min) & (ind_cols <= x_max))] = 1
    danger_map[np.where(empty > 0)] += 1

# Applies a line to the grid
def apply_line(line, use_diag=False):
    x1, x2, y1, y2 = min(line[0], line[2]), max(line[0], line[2]), min(line[1], line[3]), max(line[1], line[3])
    if x1==x2: danger_map[y1:y2+1, x1] += 1
    elif y1==y2: danger_map[y1 , x1:x2+1] += 1
    elif use_diag: apply_diag(line)
    return(0)

# ---- Part One ----
np.fromiter(map(apply_line, data), dtype=np.int)
print('Part One Answer:', np.sum(danger_map >= 2))

# ---- Part Two ----
danger_map = np.zeros(shape=(grid_size,grid_size), dtype=int)
np.fromiter(map(apply_line, data, np.full(len(data), True)), dtype=np.int)
print('Part Two Answer:', np.sum(danger_map >= 2))