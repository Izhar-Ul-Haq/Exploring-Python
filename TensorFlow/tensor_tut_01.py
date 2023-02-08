print("Tensor flow 101")
import numpy as np
import tensorflow as tf
# 1-D Tensor
tensor_1d = np.array([1.3, 1, 4.0, 23.99])
print(tensor_1d)
print(tensor_1d[0])
print(tensor_1d[1])
print(tensor_1d[2])
print(tensor_1d[3])
# 1-D Tensor
tensor_2d = np.array([
    [1.3, 1, 4.0, 2.99],
    [3, 12, 43.0, 223.99],
    [33, 12, 432.0, 3.99]
    ])
print(tensor_2d)
print(tensor_2d[0][0])
print(tensor_2d[0][1])
print(tensor_2d[0][2])
print(tensor_2d[0][3])



