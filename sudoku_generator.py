import math
import random

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


class SudokuGenerator:
    '''
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
    '''

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(row_length)]
                      for _ in range(row_length)]

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''

    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''

    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) if num != 0 else '.' for num in row))

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''

    def valid_in_col(self, col, num):
        return num not in [self.board[row][col] for row in range(self.row_length)]

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''

    def valid_in_box(self, row_start, col_start, num):
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if self.board[row][col] == num:
                    return False

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''

    def is_valid(self, row, col, num):
        return (self.valid_in_row(row, num) and
                self.valid_in_col(col, num) and
                self.valid_in_box(row - row % 3, col - col % 3, num))

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''

    def fill_box(self, row_start, col_start):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                self.board[row][col] = nums.pop()

    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''

    def fill_diagonal(self):
        for i in range(0, self.row_length, 3):
            self.fill_box(i, i)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
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

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''


def remove_cells(self):  # Sagan
    # This method removes the appropriate number of cells from the board.
    # It does so by randomly generating (row, col) coordinates of the board and
    # setting the value to 0.
    # Note: Be careful not to remove the same cell multiple times.
    # A cell can only be removed once.
    # This method should be called after generating the Sudoku solution.

    pass


class Cell:
    def __init__(self, value, row, col, screen):  # Sagan
        # Constructor for the Cell class
        pass

    def set_cell_value(self, value):  # Sagan
        # Setter for this cell’s value
        pass

    def set_sketched_value(self, value):  # Sagan
        # Setter for this cell’s sketched value
        pass

    def draw(self):  # Sagan
        # Draws this cell, along with the value inside it.
        # If this cell has a nonzero value, that value is displayed.
        # Otherwise, no value is displayed in the cell.
        # The cell is outlined red if it is currently selected.

        pass


class Board:
    def __init__(self, width, height, screen, difficulty):  # Sagan
        # Constructor for the Board class.
        # screen is a window from PyGame.
        # difficulty is a variable to indicate if the user chose easy medium, or hard.

        pass

    def draw(self):  # Sagan
        # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        # Draws every cell on this board.

        pass

    def select(self, row, col):  # Sagan
        # Marks the cell at (row, col) in the board as the current selected cell.
        # Once a cell has been selected, the user can edit its value or sketched value.

        pass

    def click(self, row, col):
        if row > Cell.CELL_SIZE * self.height or col > Cell.CELL_SIZE * self.width:
            return None

        return (row // Cell.CELL_SIZE + 1, col // Cell.CELL_SIZE + 1)

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
            [Cell(board[i][j], i, j, screen, self.font) for j in range(width)] for i in range(height)]
        self.cells = [
            [Cell(board[i][j], i, j, screen, self.font) for j in range(width)] for i in range(height)]

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


'''
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
'''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
