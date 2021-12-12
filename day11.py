import numpy as np

# ---- Load Data ----
data = np.genfromtxt('data/day11.txt', delimiter=1, dtype=int)
rows, cols = data.shape

def step(n):
    global data
    data = data + 1
    while(len(np.where(data>9)[0]) > 0):
        substep()
    return(len(np.where(data==0)[0]))

def substep():
    global data
    flashes = np.where(data > 9)
    mask = (data > 9).astype(int)

    right = np.roll(mask, 1)
    right[:,0] = 0

    left = np.roll(mask, -1)
    left[:,cols-1] = 0

    down = np.roll(mask, cols)
    down[0] = 0

    up = np.roll(mask, -cols)
    up[cols-1] = 0

    down_left = np.roll(mask, cols-1)
    down_left[0] = 0
    down_left[:,cols-1] = 0

    down_right = np.roll(mask, cols+1)
    down_right[0] = 0
    down_right[:,0] = 0

    up_left = np.roll(mask, -cols - 1)
    up_left[cols-1] = 0
    up_left[:,cols-1] = 0

    up_right = np.roll(mask, -cols + 1)
    up_right[cols-1] = 0
    up_right[:,0] = 0
    
    updates = right + left + down + up + down_left + down_right + up_left + up_right
    data[flashes] = 0
    updates[np.where(data==0)] = 0
    data = data + updates

num_steps = 2000
result = np.fromiter(map(step,  np.zeros(num_steps, dtype=np.int)), dtype=np.int)
print('Part One Answer:', sum(result[:100]))
print('Part Two Answer:', np.where(result==100)[0][0] + 1)



