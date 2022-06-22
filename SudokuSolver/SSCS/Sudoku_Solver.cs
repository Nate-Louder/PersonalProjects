using system

class Sudoku_Solver {

    static const int N = 9;

    Sudoku_Solver(int board[N][N])
    {
        this.board = board;
    }

    static bool Solve(int row, int col)
    {
        
    }

    static bool CheckRow(int row, int n)
    {
        for (int i = 0; i <= 9; i++)
        {
            if (this.board[row][i] == n)
            {
                return false;
            }
        }

        return true;
    }

    static bool CheckColumn(int col, int n)
    {
        for (int i = 0; i <= 9; i++)
        {
            if (this.board[i][col] == n)
            {
                return false;
            }
        }

        return true;
    }

    static bool CheckSquare(int row, int col, int n)
    {
        x = row - row % 3;
        y = col - col % 3;

        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (this.board[x + i][y + j] == n)
                {
                    return false;
                }
            }
        }

        return true;

    }

}