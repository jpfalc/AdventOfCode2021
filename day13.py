import numpy as np

# ---- Load Data ----
def parse_fold(str):
    if str.decode() == 'fold along y': return (0)
    else: return(1)
folds = np.loadtxt('data/day13_folds.txt', converters={0: parse_fold}, delimiter='=', dtype=int)

dots = np.loadtxt('data/day13_dots.txt', delimiter=',', dtype=int)
x_vals, y_vals = dots[:,0], dots[:,1]
max_y, max_x = max(y_vals)+1, max(x_vals)+1


image = np.zeros((max_y, max_x), dtype=int)
image[y_vals,x_vals] = 1


def print_image(img):
    final_rows, final_cols = img.shape
    for i in range(final_rows):
        str = ''
        for j in range(final_cols):
            if img[i][j] == 1:
                str = str + '#'
            else: str = str + ' '
        print(str)

# ---- Iterator Function
def fold(i, axis):
    global image
    
    if axis==0: # fold along y axis
        arr1, arr2 = image[:i, :], np.flip(image[i+1:, :], axis=0)
    else: # fold along x axis
        arr1, arr2 = image[:,:i], np.flip(image[:,i+1:], axis=1)
    arr1_rows, arr1_cols = arr1.shape
    arr2_rows, arr2_cols = arr2.shape
    final_rows, final_cols = max(arr1_rows, arr2_rows), max(arr1_cols, arr2_cols)

    arr1 = np.pad(arr1, ((final_rows - arr1_rows,0), (final_cols - arr1_cols,0)), mode='constant', constant_values=0)
    arr2 = np.pad(arr2, ((0,final_rows - arr2_rows), (0,final_cols - arr2_cols)), mode='constant', constant_values=0)


    image = np.clip(arr1 + arr2, a_min=0, a_max=1)
    return(np.sum(image))

# ---- Part One ----
result = np.fromiter(map(fold, folds[:,1], folds[:,0]), dtype=np.int)
print('Part One Answer:', result[0])

# ---- Part Two ----
print('Part Two Answer:')
np.set_printoptions(threshold=1000, linewidth=np.inf)
print_image(image)