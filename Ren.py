def transpose(matrix):
    """
    Returns the transpose of the input matrix.
    """
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    transposed = [[0 for _ in range(n_rows)] for _ in range(n_cols)]
    for i in range(n_rows):
        for j in range(n_cols):
            transposed[j][i] = matrix[i][j]
    return transposed


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
transposed = transpose(matrix)
print(transposed)