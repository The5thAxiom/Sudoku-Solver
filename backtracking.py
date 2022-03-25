"""
A sudoku solver which uses backtracking
The5thAxiom 20220325
"""
import numpy as np
from pprint import pprint

sudokuGrid = list[list[int]]

def getUnfilledCell(grid: sudokuGrid) -> tuple[int, int]:
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return (x, y)
    return (-1, -1)

def isSafe(grid: sudokuGrid, i: int, j: int, e: int) -> bool:
    for x in range(0, 9):
        for y in range(0, 9):
            if (x == i or y == j) and grid[x][y] == e:
                return False
    return True
    # how to check the boxes for each coordinate

def sudoku(grid: sudokuGrid) -> bool:
    i, j = getUnfilledCell(grid)
    if (i == -1 and j == -1):
        pprint(grid)
        return True
    else:
        for e in range(1, 10):
            if (isSafe(grid, i, j, e)):
                grid[i][j] = e
                if sudoku(grid):
                    return True
                grid[i][j] = 0
        return False

board3 = [
    [0, 1, 0, 5, 6, 0, 0, 0, 0],
    [0, 8, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 3],

    [5, 3, 0, 2, 0, 0, 0, 0, 4],
    [0, 0, 9, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 7, 0, 0, 0, 0, 0],

    [3, 0, 5, 0, 0, 0, 8, 7, 0],
    [0, 2, 6, 0, 5, 1, 0, 0, 0],
    [8, 9, 0, 0, 7, 3, 0, 5, 6]
]

if __name__ == "__main__":
    sudoku(board3)

