from operator import pos
import numpy as np

# ---- Load Data ----
data = np.loadtxt('data/day7.txt', delimiter=',', dtype=int)
max_position = np.max(data)
possible_positions = np.arange(np.max(data) + 1, dtype=np.int64)
data_adjusted = np.concatenate([data, possible_positions])
position_counts = np.unique(data_adjusted, return_counts=True)[1] - 1

# Cost function for part 2
def cost_part2(x):
    return sum(range(x+1))

# Returns array of costs to move crabs to various positions
def get_position_cost(n, part_two=False):
    distance_from_pos = np.abs(possible_positions - n)
    if (part_two): distance_from_pos = np.fromiter(map(cost_part2,  distance_from_pos), dtype=np.int64)
    return(sum(np.multiply(distance_from_pos, position_counts)))

# ---- Part One ----
fuel_costs = np.fromiter(map(get_position_cost,  possible_positions), dtype=np.int64)
print('Part One Answer:', min(fuel_costs))

# ---- Part Two ----
fuel_costs = np.fromiter(map(get_position_cost,  possible_positions, np.full(len(possible_positions), True)), dtype=np.int64)
print('Part Two Answer:', min(fuel_costs))
