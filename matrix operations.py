import numpy as np

# Function to perform matrix addition
def matrix_addition(matrix1, matrix2):
    return np.add(matrix1, matrix2)

# Function to perform matrix subtraction
def matrix_subtraction(matrix1, matrix2):
    return np.subtract(matrix1, matrix2)

# Function to perform matrix multiplication
def matrix_multiplication(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

# Example matrices for testing
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Test the functions
print("Matrix Addition:")
print(matrix_addition(A, B))

print("\nMatrix Subtraction:")
print(matrix_subtraction(A, B))

print("\nMatrix Multiplication:")
print(matrix_multiplication(A, B))
