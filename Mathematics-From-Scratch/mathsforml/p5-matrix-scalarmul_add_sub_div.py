##matrix scalar multiplication
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# scalar = 2
# # result_matrix = [[element * scalar for element in row] for row in matrix]
##or
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         matrix[i][j]=matrix[i][j]*scalar
# # Print the result matrix
# print("Result Matrix (Matrix-Scalar Multiplication):")
# for row in matrix:
#     print(row)

##matrix addition
m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
res=[[m1[i][j]+m2[i][j] for j in range(len(m1))] for i in range(len(m1))]


for i in res:
    print(i)