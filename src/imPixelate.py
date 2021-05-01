import numpy as np
import numba

@numba.njit()
def pix(img, r = None):
    [h, w] = img.shape
    if not r:
        r = min(h, w)//150
    image = img.copy()
    for row_i in range(0, h+r, 2*r):
        for column_i in range(0, w+r, 2*r):
            row_lower = row_i-r if row_i-r >= 0 else 0
            row_upper = row_i+r if row_i+r <= h else h
            column_lower = column_i-r if column_i-r >= 0 else 0
            column_upper = column_i+r if column_i+r <= w else w
            neighborings = image[row_lower:row_upper, column_lower:column_upper]
            mean = np.mean(neighborings)
            image[row_lower:row_upper, column_lower:column_upper] = mean
    return image





