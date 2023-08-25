"""
2D Matrix is given.  Each cell has cost associated with it for processing.
We need to start from 0,0 cell and go till n-1,n-1 cell
We can go only the right or down cell from the current cell

Find the way in which the cost is minimum
"""
def findMinCost(twoDArray, row, col):
    if row == -1 or col == -1:
        return float('inf')
    elif row == 0 and col == 0:
        return twoDArray[0][0]
    else:
        op1 = findMinCost(twoDArray, row-1, col)
        op2 = findMinCost(twoDArray, row, col-1)
        return twoDArray[row][col] + min(op1,op2)


# There are only two possibilities to move from one cell
# If we are at 0,0 it,s row+1(down) and col+1(right)
# If we just keep on moving our base condition becomes
# if row=4 and col =4 return its cost
# else move in both direction and take min of both's cost and also add it into currnt cell cost

def find_min_cost_practice(matrix, row, col):
    if row == 4 and col == 4:
        return matrix[row][col]
    elif row == 4:
        return matrix[row][col] + find_min_cost_practice(matrix, row, col+1)
    elif col == 4:
        return matrix[row][col] + find_min_cost_practice(matrix, row+1, col)
    else:
        way1 = find_min_cost_practice(matrix, row+1, col)
        way2 = find_min_cost_practice(matrix, row, col+1)
        return matrix[row][col] + min(way1, way2)

TwoDList = [[4,7,8,6,4],
            [6,7,3,9,2],
            [3,8,1,2,4],
            [7,1,7,3,7],
            [2,9,8,9,3]
            ]

print(findMinCost(TwoDList, 4,4))
print(find_min_cost_practice(TwoDList, 0,0))