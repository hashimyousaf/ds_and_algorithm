"""
2D Matrix is given.  Each cell has cost associated with it for processing.
We need to start from 0,0 cell and go till n-1,n-1 cell
We can go only the right or down cell from the current cell
We are given total cost to reach the last cell

Find the number of ways to reach end of the matrix with given total cost
"""

# Number of paths to reach the last cell with given cost in 2D array

def numberOfPaths(twoDArray, row, col, cost):
    if cost < 0:
        return 0
    elif row == 0 and col == 0:
        if twoDArray[0][0] - cost == 0:
            return 1
        else:
            return 0
    elif row == 0:
        return numberOfPaths(twoDArray, 0, col-1, cost - twoDArray[row][col] )
    elif col == 0:
        return numberOfPaths(twoDArray, row-1, 0, cost - twoDArray[row][col] )
    else:
        op1 = numberOfPaths(twoDArray, row -1, col, cost - twoDArray[row][col] )
        op2 = numberOfPaths(twoDArray, row, col-1, cost - twoDArray[row][col] )
        return op1 + op2

# Starting from 0,0
# go only col+1(right) and row +1(down)
# add the cost of the next cell to be and make your base condition here.
# if cost > given_cost return 0
# if row == 3 and col == 3 return its value(This is the end) and if reaching end with given cost - current = 0 then
#    return 1 else return 0
# else keep going right and down and save its value and get min of it


# Top dows implementation practice
def number_of_ways_to_reach_end(matrix, row, col, max_cost):
    if max_cost < 0:
        return 0
    elif row == 3 and col == 3:
        if max_cost - matrix[row][col] == 0:
            return 1
        else:
            return 0
    elif row == 3:
        return number_of_ways_to_reach_end(matrix, row, col+1, max_cost - matrix[row][col])
    elif col == 3:
        return number_of_ways_to_reach_end(matrix, row+1, col, max_cost - matrix[row][col])
    else:
        op1 = number_of_ways_to_reach_end(matrix, row, col+1, max_cost - matrix[row][col])
        op2 = number_of_ways_to_reach_end(matrix, row+1, col, max_cost - matrix[row][col])
        return op1 + op2




TwoDList = [[4,7,1,6],
           [5,7,3,9],
           [3,2,1,2],
           [7,1,6,3]
           ]
print(numberOfPaths(TwoDList, 3,3, 25))                 # Bottom up approach
print(number_of_ways_to_reach_end(TwoDList, 0,0, 25))   # Top down approach