# def f(i, values = []):
#     values.append(i)
#     print (values)
#     return values
# f(1)
# f(2)
# f(3)
# Rotate a image matrix NxN to 90 degree

# For example
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]

def rotate_matrix_90_degree(matrix = []):
    rotated_matrix = []
    list1 = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            list1.append(matrix[col][row])
        rotated_matrix.insert( 0, list1 )
        list1 = []
    print(rotated_matrix)



source_matrix = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
print(rotate_matrix_90_degree(source_matrix))