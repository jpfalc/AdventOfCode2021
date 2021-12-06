import numpy as np

# ---- Load Data ----
data = np.loadtxt('data/day6.txt', delimiter=',', dtype=int)
data_adjusted = np.concatenate([data, np.arange(9, dtype=np.int64)])
ages_original = np.unique(data_adjusted, return_counts=True)[1] - 1

# Iterator function
def tick(n):
    global ages
    num_new = ages[0]
    ages[0] = 0
    ages = np.roll(ages, -1)
    ages[8] += num_new
    ages[6] += num_new
    return(np.sum(ages, dtype=np.int64))

# ---- Part One ----
num_iterations = 80
ages = np.copy(ages_original)
result = np.fromiter(map(tick,  np.zeros(num_iterations, dtype=np.int64)), dtype=np.int64)
print('Part One Answer:', result[-1])

# ---- Part Two ----
num_iterations = 256
ages = np.copy(ages_original)
result = np.fromiter(map(tick,  np.zeros(num_iterations, dtype=np.int64)), dtype=np.int64)
print('Part Two Answer:', result[-1])