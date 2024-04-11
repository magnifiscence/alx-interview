#!/usr/bin/python3
"""N queens puzzle"""
import sys


def isSafe(board, row, col, n):
    """Check if a queen can be placed on board[row][col]"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solveNQUtil(board, col, n):
    """Use backtracking to solve N queens problem"""
    if col == n:
        lat = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    lat.append([i, j])
        print(lat)
        return True
    res = False
    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 1
            res = solveNQUtil(board, col + 1, n) or res
            board[i][col] = 0
    return res


def nqueens(n):
    """Solve the N queens problem"""
    if n < 4:
        print("N must be at least 4")
        return False
    board = [[0 for i in range(n)] for j in range(n)]
    solveNQUtil(board, 0, n)
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    nqueens(n)
