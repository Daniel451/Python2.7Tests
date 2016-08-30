import numpy as np

# arr.shape -> (2, 3, 2)
arr = np.array([[[8,  3],
                 [4,  5],
                 [6,  2]],

                [[9,  0],
                 [1, 10],
                 [7, 11]]])

# check_elements.shape -> (3, 2)
# generally: (n, 2)
check_elements = np.array([[4, 5], [9, 0], [7, 11]])

# rslt.shape -> (2, 3)
rslt = np.zeros((arr.shape[0], arr.shape[1]), dtype=np.bool)

for i, j in np.ndindex((arr.shape[0], arr.shape[1])):
    if arr[i, j] in check_elements:
        rslt[i, j] = True
    else:
        rslt[i, j] = False

print(rslt)

print(np.transpose(np.nonzero(rslt)))
