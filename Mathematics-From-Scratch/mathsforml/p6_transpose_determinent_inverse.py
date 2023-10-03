# ##program 1 traspose
# m1 = [
#     [1, 2],
#     [4, 5],
# ]
#
# traspose=[[0 for i in range(len(m1))] for j in range(len(m1))]
#
#
# for i in range(len(m1)):
#     for j in range(len(m1)):
#         traspose[i][j]=m1[j][i]
#
# print(traspose)

# ##program 2 inverse method 1:
# Define the 2x2 matrix
matrix = [[3, 4],
          [2, 5]]

# Calculate the determinant
det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

# Check if the matrix is invertible
if det == 0:
    print("The matrix is not invertible.")
else:
    # Calculate the inverse
    inverse_matrix = [[matrix[1][1] / det, -matrix[0][1] / det],
                      [-matrix[1][0] / det, matrix[0][0] / det]]

    print("Original matrix:")
    for row in matrix:
        print(row)

    print("Inverse matrix:")
    for row in inverse_matrix:
        print(row)

