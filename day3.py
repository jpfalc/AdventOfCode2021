import numpy as np
from scipy.stats import mode

# ---- Load Data ----
data = np.genfromtxt('data/day3.txt', delimiter=1, dtype=int)
num_rows, num_cols = data.shape

# ---- Part One ----
bits = mode(data, axis=0).mode.flatten()
gamma = bits.dot(2**np.arange(bits.size)[::-1])
epsilon = (1-bits).dot(2**np.arange((1-bits).size)[::-1])
print('Part One Answer:', gamma*epsilon)

# ---- Part Two ----
def filter_o2(i):
    global data_pt2
    rows = data_pt2.shape[0]
    ones = data_pt2.sum(axis=0)[i] 
    zeroes = rows - ones
    if rows <= 1:
        return(ones)
    if ones >= zeroes:
        data_pt2 = data_pt2[np.where(data_pt2[:,i] == 1)]
        return(1)
    else:
        data_pt2 = data_pt2[np.where(data_pt2[:,i] == 0)]
        return(0)

def filter_co2(i):
    global data_pt2
    rows = data_pt2.shape[0]
    ones = data_pt2.sum(axis=0)[i] 
    zeroes = rows - ones
    if rows <= 1:
        return(ones)
    if ones < zeroes:
        data_pt2 = data_pt2[np.where(data_pt2[:,i] == 1)]
        return(1)
    else:
        data_pt2 = data_pt2[np.where(data_pt2[:,i] == 0)]
        return(0)

column_list = np.arange(num_cols)

data_pt2 = np.copy(data)
result = np.fromiter(map(filter_o2, column_list), dtype=int)
rating_o2 = result.dot(2**np.arange(result.size)[::-1])

data_pt2 = np.copy(data)
result = np.fromiter(map(filter_co2, column_list), dtype=int)
rating_co2 = result.dot(2**np.arange(result.size)[::-1])
print('Part Two Answer:', rating_o2*rating_co2)