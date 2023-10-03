# Define a matrix as a list of lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Define a vector as a list
vector = [2,
          3,
          4]

# Initialize the result vector with zeros
result_vector = [0] * len(matrix)
# Perform matrix multiplication
for i in range(len(matrix)):
    for j in range(len(vector)):
        result_vector[i] += matrix[i][j] * vector[j]


# Print the result vector
print(result_vector)


