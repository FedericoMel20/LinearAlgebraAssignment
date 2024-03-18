import numpy as np

# Function to calculate the determinant of a matrix
def matrix_determinant(matrix):
    return np.linalg.det(matrix)

# Example matrices for testing
A = np.array([[5, -2], [3, 14]])
B = np.array([[4, 1, 5], [7, 2, -1], [-5, 11, 3]])

# Test the functions
print("\nMatrix A Determinant:")
print(matrix_determinant(A))

print("\nMatrix B Determinant:")
print(matrix_determinant(B))
