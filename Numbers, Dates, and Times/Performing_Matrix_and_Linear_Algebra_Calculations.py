# coding=utf-8

"""
Problem

You need to perform matrix and linear algebra operations, such as matrix multiplication, finding 
determinants, solving linear equations, and so on.

Solution

The NumPy library has a matrix object that can be used for this purpose. Matrices are somewhat similar to 
the array objects described in "Calculating with Large Numerical Arrays", but follow linear algebra rules 
for computation. Here is an example that illustrates a few essential features:
"""
import numpy as np
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
m
# Returns matrix([[ 1, -2,  3],
#                 [ 0,  4,  5],
#                 [ 7,  8, -9]])

# Return transpose
m.T
# Returns matrix([[ 1,  0,  7],
#                 [-2,  4,  8],
#                 [ 3,  5, -9]])

# Return inverse
m.I
# Returns matrix([[ 0.33043478, -0.02608696,  0.09565217],
#                 [-0.15217391,  0.13043478,  0.02173913],
#                 [ 0.12173913,  0.09565217, -0.0173913 ]])

# Create a vector and multiply
v = np.matrix([[2],[3],[4]])
v
# Returns matrix([[2],
#                 [3],
#                 [4]])
m * v
# Returns matrix([[ 8],
#                 [32],
#                 [ 2]])

"""
More operations can be found in the numpy.linalg subpackage. For example:
"""
import numpy.linalg

# Determinant
numpy.linalg.det(m)
# Returns -229.99999999999983

# Eigenvalues
numpy.linalg.eigvals(m)
# Returns array([-13.11474312,   2.75956154,   6.35518158])

# Solve for x in mx = v
x = numpy.linalg.solve(m, v)
x
# Returns matrix([[ 0.96521739],
#                 [ 0.17391304],
#                 [ 0.46086957]])
m * x
# Returns matrix([[ 2.],
#                 [ 3.],
#                 [ 4.]])
v
# Returns matrix([[2],
#                 [3],
#                 [4]])

"""
Discussion

Linear algebra is obviously a huge topic that’s far beyond the scope of this cookbook. However, if you 
need to manipulate matrices and vectors, NumPy is a good starting point. 
Visit http://www.numpy.org for more detailed information.
"""
