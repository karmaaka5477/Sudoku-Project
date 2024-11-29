import pygame
import random
from enum import Enum
from difficulty import Difficulty


"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


class Color(Enum):
    LIGHT_GREEN = (209, 255, 164)
    GREEN = (134, 196, 71)
    STEEL_BLUE = (99, 125, 142)


class SudokuGenerator:
    """
        create a sudoku board - initialize class variables and set up the 2D board
        This should initialize:
        self.row_length		- the length of each row
        self.removed_cells	- the total number of cells to be removed
        self.board			- a 2D list of ints to represent the board
        self.box_length		- the square root of row_length

        Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

        Return:
        None
    """

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
        self.box_length = int(self.row_length**0.5)

    """
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    """

    def get_board(self):
        return self.board

    """
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    """

    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) if num != 0 else "." for num in row))

    """
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row

	Return: boolean
    """

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    """
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column

	Return: boolean
    """

    def valid_in_col(self, col, num):
        return num not in [self.board[row][col] for row in range(self.row_length)]

    """
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    """

    def valid_in_box(self, row_start, col_start, num):
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if self.board[row][col] == num:
                    return False
        return True

    """
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    """

    def is_valid(self, row, col, num):
        return (
            self.valid_in_row(row, num)
            and self.valid_in_col(col, num)
            and self.valid_in_box(row - row % 3, col - col % 3, num)
        )

    """
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    """

    def fill_box(self, row_start, col_start):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                self.board[row][col] = nums.pop()

    """
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    """

    def fill_diagonal(self):
        for i in range(0, self.row_length, 3):
            self.fill_box(i, i)

    """
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled

	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    """

    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    """
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    """

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    """
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called

    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    """

    def remove_cells(self):  # Sagan
        # This method removes the appropriate number of cells from the board.
        # It does so by randomly generating (row, col) coordinates of the board and
        # setting the value to 0.
        # Note: Be careful not to remove the same cell multiple times.
        # A cell can only be removed once.
        # This method should be called after generating the Sudoku solution.

        empty_cells = Difficulty.get_difficulty().value

        a = [0] * empty_cells + [1] * (self.row_length**2 - empty_cells)

        random.shuffle(a)

        for i in range(self.row_length):
            for j in range(self.row_length):
                if a[i * self.row_length + j] == 0:
                    self.board[i][j] = 0


class Cell:
    HIGHLIGHT_COLOR = Color.GREEN.value
    SELECTED_COLOR = Color.STEEL_BLUE.value
    screen = None

    @classmethod
    def init(cls, x, y, screen, font):
        cls.screen = screen
        cls.font = font
        cls.board_x = x
        cls.board_y = y

    @classmethod
    def get_cell_size(cls):
        return cls.screen.get_height() / 9.5

    def __init__(self, value, row, col):
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col

    def set_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self, selected=False, highlighted=False):
        cell_x = Cell.board_x + self.col * Cell.get_cell_size()
        cell_y = Cell.board_y + self.row * Cell.get_cell_size()

        if selected or highlighted:
            pygame.draw.rect(
                Cell.screen,
                Cell.SELECTED_COLOR if selected else Cell.HIGHLIGHT_COLOR,
                pygame.Rect(
                    cell_x + 1, cell_y + 1, Cell.get_cell_size(), Cell.get_cell_size()
                ),
                3,
                border_radius=5,
            )

        if self.value == 0:
            if self.sketched_value == 0:
                return
            text = Cell.font.render(str(self.sketched_value), True, (100, 100, 100))
            Cell.screen.blit(text, (cell_x + 10, cell_y + 10))
            return

        text = Cell.font.render(str(self.value), True, (20, 20, 20))
        text_width, text_height = Cell.font.size(str(self.value))
        Cell.screen.blit(
            text,
            (
                cell_x + (Cell.get_cell_size() - text_width) // 2,
                cell_y + (Cell.get_cell_size() - text_height) // 2,
            ),
        )


class Board:
    def __init__(self, x, y, width, height, screen, font, board):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.font = font
        self.selected_cell = None
        self.highlighted_cell = None
        self.update_board(width, height, screen, board)

    def draw(self):

        # draws row separating lines
        for i in range(1, self.height):
            pygame.draw.line(
                self.screen,
                (30, 30, 30),
                (self.x, self.y + i * Cell.get_cell_size()),
                (
                    self.x + self.width * Cell.get_cell_size(),
                    self.y + i * Cell.get_cell_size(),
                ),
                2 + (i % 3 == 0) * 2,
            )

        # draws column separating lines
        for i in range(1, self.width):
            pygame.draw.line(
                self.screen,
                (30, 30, 30),
                (self.x + i * Cell.get_cell_size(), self.y),
                (
                    self.x + i * Cell.get_cell_size(),
                    self.y + self.height * Cell.get_cell_size(),
                ),
                2 + (i % 3 == 0) * 2,
            )

        # draws cells (their numbers and sketched numbers)
        for row in self.cells:
            for cell in row:
                cell.draw(
                    selected=cell is self.selected_cell,
                    highlighted=cell is self.highlighted_cell,
                )

    def select(self, row, col):
        self.selected_cell = self.cells[col][row]

    def get_cell(self, row, col):
        if (
            row > self.y + Cell.get_cell_size() * self.height
            or col > self.x + Cell.get_cell_size() * self.width
            or row < self.y
            or col < self.x
        ):
            return None

        row_idx = int((row - self.y) // Cell.get_cell_size())
        col_idx = int((col - self.x) // Cell.get_cell_size())

        return (row_idx, col_idx)

    def update_hover(self, row, col):
        curr = self.get_cell(row, col)
        if curr is None:
            self.highlighted_cell = None
            return

        row_idx, col_idx = curr

        if self.original_cells[col_idx][row_idx].value == 0:
            self.highlighted_cell = self.cells[col_idx][row_idx]
        else:
            self.highlighted_cell = None

        return curr

    def click(self, row, col):
        curr = self.get_cell(row, col)
        if curr is None:
            self.selected_cell = None
            return

        row_idx, col_idx = curr

        if self.original_cells[col_idx][row_idx].value == 0:
            self.select(row_idx, col_idx)
        else:
            self.selected_cell = None

        return curr

    def clear(self):
        if self.selected_cell is None:
            return

        cell = self.selected_cell

        if self.original_cells[cell.row][cell.col].value == 0:
            return

        self.place_number(0)
        self.sketch(0)

    def sketch(self, value):
        if self.selected_cell is None:
            return

        self.selected_cell.set_sketched_value(value)

    def place_number(self, value):
        if self.selected_cell is None:
            return

        self.selected_cell.set_value(value)

    def reset_to_original(self):
        for i in range(self.height):
            for j in range(self.width):
                cell = self.original_cells[i][j]
                self.cells[i][j].set_value(cell.value)
                self.cells[i][j].set_sketched_value(cell.sketched_value)

    def is_full(self):
        if self.find_empty():
            return False
        return True

    def update_board(self, width, height, screen, board):
        self.original_cells = [
            [Cell(board[i][j], i, j) for j in range(width)] for i in range(height)
        ]
        self.cells = [
            [Cell(board[i][j], i, j) for j in range(width)] for i in range(height)
        ]

    def find_empty(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.cells[i][j].value == 0:
                    return (i, j)
        return False

    def check_board(self):
        if not self.is_full():
            return False

        # Row check
        for i in range(self.height):
            s = set()
            for j in range(self.width):
                s.add(self.cells[i][j])
            if len(s) != self.width:
                return False

        # Col check
        for i in range(self.width):
            s = set()
            for j in range(self.height):
                s.add(self.cells[j][i])
            if len(s) != self.width:
                return False

        # Box check
        for i in range(0, 3, 3):
            for j in range(0, 3, 3):
                s = set()
                for k in range(3):
                    for l in range(3):
                        s.add(self.cells[i + k][j + l])
                if len(s) != 9:
                    return False

        return True


class Button:
    def __init__(self, rect: pygame.Rect):
        self.rect = rect
        self.hover = False

    def update_hover(self, x, y):
        if self.rect.collidepoint(x, y):
            if not self.hover:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            self.hover = True
        else:
            if self.hover:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            self.hover = False


"""
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
"""


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
