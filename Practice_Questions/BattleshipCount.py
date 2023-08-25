"""
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on
board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape
1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical
 cell separates between two battleships (i.e., there are no adjacent battleships).

================
Two situations:
================
If a cell is part of battleship (horizontal or verticle), then don't increment the count
If a cell is not surrounded by X from left and from top, then increment the count because it is a start of battleship
But to check left need to make sure that cell is not 0th column and to check top need to make sure that cell is not on 0th row
"""


class Solution:
    def countBattleships(self, board):
        count = 0
        m, n = len(board), len(board[0])  # m = rows, n = columns

        for r in range(m):
            for c in range(n):
                if board[r][c] == "X":
                    if (r == 0 or board[r - 1][c] == ".") and (c == 0 or board[r][c - 1] == "."):
                        count += 1
        return count

print(Solution().countBattleships([["X",".",".","X"],
                                   [".",".","X","X"],
                                   [".",".",".","X"]]))