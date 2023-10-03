def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    l, r = 0, len(matrix) - 1
    while l < r:
        for i in range(r - l):
            top, bottom = l, r
            topleft = matrix[top][l + i]
            matrix[top][l + i] = matrix[bottom - i][l]
            matrix[bottom - i][l] = matrix[bottom][r - i]
            matrix[bottom][r - i] = matrix[top - i][r]
            matrix[top + i][r] = topleft

        r -= 1
        l += 1


matrix =[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
rotate(matrix)
print(matrix)