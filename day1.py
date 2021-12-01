import numpy as np

# ---- Load Data ----
data = []
with open('data/day1.txt') as file:
    for line in file.readlines():
        data.append(int(line))


# ---- Part One ----
data_offset1 = [0] + data[:-1]
data_diff = np.subtract(data, data_offset1)
print('Part One Answer:', np.sum(data_diff > 0) - 1)


# ---- Part Two ----
data_offset2 = [0] + [0] + data[:-2]
sums = np.add(np.add(data, data_offset1), data_offset2)
sums_offset1 = np.append([0], sums[:-1])
sums_diff = np.subtract(sums, sums_offset1)
print('Part Two Answer:', np.sum(sums_diff > 0) - 3)

