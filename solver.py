import numpy as np
from pprint import pprint

def hasPass(board, rowDict, colDict, blockDict):
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == 0:
                continue
            rowDict[i][num] = True
            colDict[j][num] = True
            blockDict[(j//3, i//3)][num] = True # the blocks are meant to be indexed sort-of like an array with the top 3 being 0,0 1,0 and 2, 0
    return rowDict, colDict, blockDict

def putPass(board, rowDict, colDict, blockDict):
    for i in range(9):
        for j in range(9):
            for num in range(1, 10):
                if rowDict[i][num]:
                    
    return board

def solve(board):
    assert(board.shape == (9, 9))
    # these dicts store the remaining numbers for each row
    rowDict = {index: {x for x in range(1, 10)} for index in range(9)}
    colDict = {index: {x for x in range(1, 10)} for index in range(9)}
    blockDict = {(a, b): {x for x in range(1, 10)} for b in range(3) for a in range(3)}
    rowDict, colDict, blockDict = hasPass(board, rowDict, colDict, blockDict)
    board = putPass(board, rowDict, colDict, blockDict)
    rowDict, colDict, blockDict = hasPass(board, rowDict, colDict, blockDict)
    print(board)
    pprint(rowDict)
    pprint(colDict)
    pprint(blockDict)
    if 0 not in board:
        return board
    else:
        print('ab')

if __name__ == "__main__":
    board1 = np.array([
        [4, 9, 5, 0, 1, 0, 7, 6, 8],
        [0, 1, 0, 6, 4, 8, 0, 0, 9],
        [6, 8, 2, 7, 9, 5, 1, 0, 4],
        [1, 4, 0, 3, 0, 0, 9, 5, 6],
        [5, 0, 0, 1, 0, 0, 0, 7, 0],
        [7, 0, 6, 5, 0, 0, 2, 4, 0],
        [2, 0, 1, 8, 0, 7, 0, 0, 5],
        [8, 5, 4, 9, 0, 0, 0, 1, 0],
        [9, 7, 3, 4, 5, 1, 6, 0, 0],
        ])
    b1 = solve(board1)