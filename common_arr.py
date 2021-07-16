# Write a program to find the common values between two arrays

import numpy as np

a=np.array([0,  1,   2,    3,  4,   5])
b=np.array([2,  4,  1,   0,   2,   4])
print(np.intersect1d(a,b))
