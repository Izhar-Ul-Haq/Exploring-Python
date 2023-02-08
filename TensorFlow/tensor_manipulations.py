import tensorflow as tf
import numpy as np

matrix1 = np.array([(2,2,2),(2,2,2),(2,2,2)],dtype='int32')
matrix2 = np.array([(1,1,1),(1,1,1),(1,1,1)],dtype='int32')
print (matrix1)
print (matrix2)
matrix1 = tf.constant(matrix1)
matrix2 = tf.constant(matrix2)
matrix_product = tf.matmul(matrix1, matrix2)
matrix_sum = tf.add(matrix1,matrix2)
print(matrix1)
print(matrix2)
print(matrix_product)
print(matrix_sum)
matrix_3 = np.array([(2,7,2),(1,4,2),(9,0,2)],dtype='float32')
print (matrix_3)
# Matrix Determinants
matrix_det = tf.linalg.det(matrix_3)
print(matrix_det)
with tf.compat.v1.Session() as sess:
 result1 = sess.run(matrix_product)
 result2 = sess.run(matrix_sum)
 result3 = sess.run(matrix_det)
print (result1)
print (result2)
print (result3)