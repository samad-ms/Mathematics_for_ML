# Define two matrices as lists of lists
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
]

matrix2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Initialize the result matrix with zeros
result_matrix = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
# Perform matrix multiplication
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

# Print the result matrix
print("Result Matrix (Matrix-Matrix Multiplication):")
for row in result_matrix:
    print(row)
