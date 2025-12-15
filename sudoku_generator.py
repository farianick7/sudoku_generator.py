import math,random

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = 3
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
        self.solution = None

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(" ".join(str(x) for x in row))

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        for r in range(self.row_length):
            if self.board[r][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for r in range(row_start, row_start + self.box_length):
            for c in range(col_start, col_start + self.box_length):
                if self.board[r][c] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        return (self.valid_in_row(row, num) and
                self.valid_in_col(col, num) and
                self.valid_in_box(row - row % self.box_length,
                                  col - col % self.box_length, num))

    def fill_box(self, row_start, col_start):
        nums = list(range(1, self.row_length + 1))
        random.shuffle(nums)
        idx = 0
        for r in range(row_start, row_start + self.box_length):
            for c in range(col_start, col_start + self.box_length):
                self.board[r][c] = nums[idx]
                idx += 1

    def fill_diagonal(self):
        for i in range(0, self.row_length, self.box_length):
            self.fill_box(i, i)

    def fill_remaining(self, row=0, col=0):
        if col >= self.row_length and row == self.row_length - 1:
            return True
        if col >= self.row_length:
            row += 1
            col = 0
        if self.board[row][col] != 0:
            return self.fill_remaining(row, col + 1)
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining()
        self.solution = [row[:] for row in self.board]

    def remove_cells(self):
        count = self.removed_cells
        while count > 0:
            row = random.randrange(0, self.row_length)
            col = random.randrange(0, self.row_length)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count -= 1


def generate_sudoku(size, removed):
    generator = SudokuGenerator(size, removed)
    generator.fill_values()
    generator.remove_cells()
    return generator.get_board()

if __name__ == "__main__":
    board = generate_sudoku(9, 40) 
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))
