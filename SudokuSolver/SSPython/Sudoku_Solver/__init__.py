
from xmlrpc.client import Boolean

board_size = 9

class Sudoku_Solver():

    def __init__(this, board):
        this.board = board

    def PrintBoard(this):
        for i in range(9):
            for j in range(9):
                print (this.board[i][j], end = " ")
            print()

    def Solve(this, row, col) -> Boolean:
        
        row, col = 0

        if row == board_size - 1 and col == board_size:
            return True
        
        if col == board_size:
            col = 0
            row += 1
        
        if this.board[row][col] > 0:
            return this.Solve(row, col + 1)
        
        for i in range (1, board_size + 1, 1):
            if this.CheckRow(row, i) and this.CheckColumn(col, i) and this.CheckSquare(row, col, i):
                this.board[row][col] = i
                if this.Solve(row, col + 1):
                    return True         

    def CheckRow(this, i, n) -> Boolean:

        x = 0
        while x < 9:
            if this.board[i][x] == n:
                return False
            x += 1
        return True

    def CheckColumn(this, j, n) -> Boolean:

        x = 0
        while x < 9:
            if this.board[x][j] == n:
                return True
            x += 1
        return False

    def CheckSquare(this, row, col, n) -> Boolean:
        
        x = row - row % 3
        y = col - col % 3

        for i in range (board_size):
            for j in range(board_size):
                if this.board[i + x][j + y] == n:
                    return False
        return True
