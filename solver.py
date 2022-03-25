"""
Sudoku-Solver:
    Creating a solver for simple sudoku boards
    This implementation does NOT uses backtracking
The5thAxiom 20211205
under GNU GPL v2
"""

import numpy as np
from pprint import pprint

# goes through the board and keeps track of what is remaining in every row, block and column
def hasPass(board, rowDict, colDict, blockDict):
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == 0:
                continue
            # remove the number at the current spot from the remaining sets for the respective row, block and column
            rowDict[i] = rowDict[i] - {num}
            colDict[j] = colDict[j] - {num}
            blockDict[(i//3, j//3)] = blockDict[(i//3, j//3)] - {num}
    return rowDict, colDict, blockDict

def putPass(board, rowDict, colDict, blockDict):
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0: # if the spot is already filled, we don't need to do anything
                continue
            if len(rowDict[i]) == 1: # if there is only 1 remaining value for the row to be complete
                board[i][j] = list(rowDict[i])[0]
            elif len(colDict[j]) == 1:# if there is only 1 remaining value for the col to be complete
                board[i][j] = list(colDict[j])[0]
            elif len(blockDict[(i//3, j//3)]) == 1:# if there is only 1 remaining value for the block to be complete
                board[i][j] = list(blockDict[(i//3, j//3)])[0]
            elif len(rowDict[i] & colDict[j]) == 1:# if there is only 1 possible value at that intersection of a row and a column
                board[i][j] = list(rowDict[i] & colDict[j])[0]
            elif len(rowDict[i] & blockDict[(i//3, j//3)]) == 1:# if there is only 1 possible value at that intersection of a row and a block
                board[i][j] = list(rowDict[i] & blockDict[(i//3, j//3)])[0]
            elif len(colDict[j] & blockDict[(i//3, j//3)]) == 1:# if there is only 1 possible value at that intersection of a block and a column
                board[i][j] = list(colDict[j] & blockDict[(i//3, j//3)])[0]
            elif len(colDict[j] & rowDict[i] & blockDict[(i//3, j//3)]) == 1:# if there is only 1 possible value at that intersection of a row, a block and a column
                board[i][j] = list(colDict[j] & rowDict[i] & blockDict[(i//3, j//3)])[0]
            else:
                continue
    return board

def solve(board):
    assert(board.shape == (9, 9)) # just to verify that the board is complete
    # these dicts store the remaining numbers for each row
    rowDict = {index: {x for x in range(1, 10)} for index in range(9)}
    colDict = {index: {x for x in range(1, 10)} for index in range(9)}
    blockDict = {(a, b): {x for x in range(1, 10)} for b in range(3) for a in range(3)}
    rowDict, colDict, blockDict = hasPass(board, rowDict, colDict, blockDict)
    #while 0 in board: # run unless the board is compelete (this could cause problems for a board unsolvable by my technique)
    for i in range(1000):
        board = putPass(board, rowDict, colDict, blockDict)
        # pprint(rowDict)
        # pprint(colDict)
        # pprint(blockDict)
        rowDict, colDict, blockDict = hasPass(board, rowDict, colDict, blockDict)
    return board


if __name__ == "__main__":
    # board1 = np.array([
    #     [4, 9, 5, 0, 1, 0, 7, 6, 8],
    #     [0, 1, 0, 6, 4, 8, 0, 0, 9],
    #     [6, 8, 2, 7, 9, 5, 1, 0, 4],
    #     [1, 4, 0, 3, 0, 0, 9, 5, 6],
    #     [5, 0, 0, 1, 0, 0, 0, 7, 0],
    #     [7, 0, 6, 5, 0, 0, 2, 4, 0],
    #     [2, 0, 1, 8, 0, 7, 0, 0, 5],
    #     [8, 5, 4, 9, 0, 0, 0, 1, 0],
    #     [9, 7, 3, 4, 5, 1, 6, 0, 0],
    # ])
    # print(board1)
    # print(solve(board1))
    # print("--------------------------------")
    # board2 = np.array([
    #     [5, 3, 0, 0, 7, 0, 0, 0, 0],
    #     [6, 0, 0, 1, 9, 5, 0, 0, 0],
    #     [0, 9, 8, 0, 0, 0, 0, 6, 0],
    #     [8, 0, 0, 0, 6, 0, 0, 0, 3],
    #     [4, 0, 0, 8, 0, 3, 0, 0, 1],
    #     [7, 0, 0, 0, 2, 0, 0, 0, 6],
    #     [0, 6, 0, 0, 0, 0, 2, 8, 0],
    #     [0, 0, 0, 4, 1, 9, 0, 0, 5],
    #     [0, 0, 0, 0, 8, 0, 0, 7, 9]
    # ])
    # print(board2)
    # print(solve(board2))
    print("--------------------------------")
    board3 = np.array([
        [0, 1, 0, 5, 6, 0, 0, 0, 0],
        [0, 8, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 3],

        [5, 3, 0, 2, 0, 0, 0, 0, 4],
        [0, 0, 9, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],

        [3, 0, 5, 0, 0, 0, 8, 7, 0],
        [0, 2, 6, 0, 5, 1, 0, 0, 0],
        [8, 9, 0, 0, 7, 3, 0, 5, 6]
    ])
    print(board3)
    print(solve(board3))
    print("--------------------------------")
