from collections import defaultdict
from typing import List


class NQueens(object):
    def __init__(self, n):
        # dale - valley or row - column
        # hill - uphill or row + column
        self.n = n
        self.dale_diagonals = defaultdict(int)
        self.hill_diagonals = defaultdict(int)
        self.cols_taken = defaultdict(int)
        self.queens = set()
        self.output = []

    def solve_n_queens(self) -> List[List[str]]:
        '''
            dale: row - column
            hill: row + column
        '''
        self.backtrack(0)
        return self.output

    def could_place(self, row, col):

        return (not self.dale_diagonals[row - col]
                and not self.hill_diagonals[row + col]
                and not self.cols_taken[col])

    def place_queen(self, row, col):
        self.cols_taken[col] = 1
        self.dale_diagonals[row - col] = 1
        self.hill_diagonals[row + col] = 1
        self.queens.add((row, col))

    def remove_queen(self, row, col):
        self.cols_taken[col] = 0
        self.dale_diagonals[row - col] = 0
        self.hill_diagonals[row + col] = 0
        self.queens.remove((row, col))

    def add_solution(self):
        solution = []
        for _, col in sorted(self.queens):
            solution.append("." * col + "Q" + "." * (self.n - 1 - col))
        self.output.append(solution)

    def backtrack(self, row):
        for col in range(self.n):
            if self.could_place(row, col):
                self.place_queen(row, col)
                if row + 1 == self.n:
                    self.add_solution()
                else:
                    self.backtrack(row + 1)
                self.remove_queen(row, col)


if __name__ == "__main__":
    obj = NQueens(4)
    print(obj.solve_n_queens())
