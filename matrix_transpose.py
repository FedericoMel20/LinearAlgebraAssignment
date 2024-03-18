import numpy as np
# Function to find the transpose of a square matrix
def matrix_transpose(matrix):
    return np.transpose(matrix)

# Example matrices for testing
A = np.array([[1, 5], [2, -1]])
B = np.array([[8, 3], [7, 4]])

#Test
print("\nMatrix A Transpose:")
print(matrix_transpose(A))

print("\nMatrix B Transpose:")
print(matrix_transpose(B))
