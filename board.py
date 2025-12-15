import pygame
from sudoku_generator import SudokuGenerator
from cell import Cell

BLACK = (0, 0, 0)

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen

        if difficulty == "easy":
            removed = 30
        elif difficulty == "medium":
            removed = 40
        else:
            removed = 50

        generator = SudokuGenerator(9, removed)
        generator.fill_values()
        self.solution = [row[:] for row in generator.solution]
        generator.remove_cells()
        puzzle = generator.get_board()

        self.original_board = [row[:] for row in puzzle]
        self.board = [row[:] for row in puzzle]

        self.cells = []
        for r in range(9):
            row_cells = []
            for c in range(9):
                row_cells.append(Cell(self.board[r][c], r, c, self.screen))
            self.cells.append(row_cells)

        self.selected_row = None
        self.selected_col = None

    def draw(self):
        cell_width = self.width // 9
        cell_height = self.height // 9

        for i in range(10):
            thickness = 3 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, BLACK,
                             (0, i * cell_height),
                             (self.width, i * cell_height),
                             thickness)
            pygame.draw.line(self.screen, BLACK,
                             (i * cell_width, 0),
                             (i * cell_width, self.height),
                             thickness)

        for r in range(9):
            for c in range(9):
                self.cells[r][c].draw(self.width, self.height)

    def select(self, row, col):
        if self.selected_row is not None and self.selected_col is not None:
            self.cells[self.selected_row][self.selected_col].selected = False
        self.selected_row = row
        self.selected_col = col
        self.cells[row][col].selected = True

    def click(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            cell_width = self.width // 9
            cell_height = self.height // 9
            col = x // cell_width
            row = y // cell_height
            return (row, col)
        return None

    def clear(self):
        if self.selected_row is None or self.selected_col is None:
            return
        r, c = self.selected_row, self.selected_col
        if self.original_board[r][c] == 0:
            self.cells[r][c].set_cell_value(0)
            self.cells[r][c].set_sketched_value(0)
            self.update_board()

    def sketch(self, value):
        if self.selected_row is None or self.selected_col is None:
            return
        r, c = self.selected_row, self.selected_col
        if self.original_board[r][c] == 0:
            self.cells[r][c].set_sketched_value(value)

    def place_number(self, value):
        if self.selected_row is None or self.selected_col is None:
            return
        r, c = self.selected_row, self.selected_col
        if self.original_board[r][c] == 0:
            self.cells[r][c].set_cell_value(value)
            self.update_board()

    def reset_to_original(self):
        self.board = [row[:] for row in self.original_board]
        for r in range(9):
            for c in range(9):
                self.cells[r][c].set_cell_value(self.board[r][c])
                self.cells[r][c].set_sketched_value(0)

    def is_full(self):
        for row in self.board:
            if 0 in row:
                return False
        return True

    def update_board(self):
        for r in range(9):
            for c in range(9):
                self.board[r][c] = self.cells[r][c].value

    def find_empty(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    return (r, c)
        return None

    def check_board(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] != self.solution[r][c]:
                    return False
        return True