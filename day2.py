from operator import pos
import numpy as np

# ---- Text Parsing Functions ----
def values_vertical(str):
    if str==b'up':
        return 1
    elif str==b'down':
        return -1
    else:
        return 0

def values_horizontal(str):
    if str==b'forward':
        return 1
    else:
        return 0


# ---- Load Data ----
data_vertical = np.loadtxt('data/day2.txt', converters={0: values_vertical}, dtype=int)
data_horizontal = np.loadtxt('data/day2.txt', converters={0: values_horizontal}, dtype=int)


# ---- Part One ----
motion_vertical = np.multiply(data_vertical[:, 0], data_vertical[:, 1])
motion_horizontal = np.multiply(data_horizontal[:, 0], data_horizontal[:, 1])
depth = -1 * sum(motion_vertical)
position = sum(motion_horizontal)
print('Part One Answer:', depth*position)


# ---- Part Two ----
aim = np.cumsum(motion_vertical, dtype=int)
depth_chg = np.multiply(motion_horizontal, aim)
depth = -1 * sum(depth_chg)
print('Part Two Answer:', depth*position)