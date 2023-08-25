
def zero_matrix(matrix):
    #matrix = mat.copy()
    rows = len(matrix)
    cols = len(matrix[0])
    row_set = set()
    col_set = set()
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_set.add(i)
                col_set.add(j)

    for i in range(rows):
        for j in range(cols):
            if (i in row_set) or (j in col_set):
                matrix[i][j] = 0
    return matrix

mat = [
        [1, 2, 3, 4, 0],
        [6, 0, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 0, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]

print(zero_matrix(mat))