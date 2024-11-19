import pygame
from sudoku_generator import Board, generate_sudoku, WIDTH, HEIGHT

pygame.font.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 32)


def main():
    sudoku_board = generate_sudoku(9, 15)
    display_board = Board(9, 9, WINDOW, FONT, sudoku_board)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                display_board.click(x, y)

        WINDOW.fill('white')
        display_board.draw()

        pygame.display.update()


if __name__ == "__main__":
    main()
