import numpy as np

# Function to find the inverse of a matrix
def matrix_inverse(matrix):
    return np.linalg.inv(matrix)

# Example matrices for testing
matrix_A = np.array([[1, 2], [3, 4]])

# Test the functions
print("\nMatrix A Inverse:")
print(matrix_inverse(matrix_A))
