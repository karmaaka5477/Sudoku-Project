import pygame
from sudoku_generator import Cell, Board, Button, generate_sudoku
from difficulty import Difficulty, DifficultyLevel

pygame.font.init()

WINDOW_WIDTH = 590 * 1.5
WINDOW_HEIGHT = 410 * 1.5
BOARD_X = 10 * WINDOW_WIDTH / 590
BOARD_Y = 10 * WINDOW_HEIGHT / 410
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
FONT = pygame.font.SysFont(None, 32)
pygame.display.set_caption("Smiski Sudoku")

Cell.init(BOARD_X, BOARD_Y, WINDOW, FONT)

main_menu_bg = pygame.image.load("assets/home_screen.jpg").convert()
game_bg = pygame.image.load("assets/play_screen.jpg").convert()

BUTTON_WIDTH = 0.135 * WINDOW_WIDTH
BUTTON_HEIGHT = 0.09 * WINDOW_HEIGHT

RESET_BUTTON_X = 0.695 * WINDOW_WIDTH
RESET_BUTTON_Y = 0.05 * WINDOW_HEIGHT

RESTART_BUTTON_X = 0.85 * WINDOW_WIDTH
RESTART_BUTTON_Y = 0.05 * WINDOW_HEIGHT

EXIT_BUTTON_X = 0.775 * WINDOW_WIDTH
EXIT_BUTTON_Y = 0.163 * WINDOW_HEIGHT


reset_easy_button = Button(
    pygame.Rect(RESET_BUTTON_X, RESET_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
)

restart_medium_button = Button(
    pygame.Rect(RESTART_BUTTON_X, RESTART_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
)

exit_hard_button = Button(
    pygame.Rect(EXIT_BUTTON_X, EXIT_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
)


def init_board():
    sudoku_board = generate_sudoku(9, Difficulty.get_difficulty().value)
    display_board = Board(BOARD_X, BOARD_Y, 9, 9, WINDOW, FONT, sudoku_board)

    return display_board


def game_loop():
    display_board = init_board()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                display_board.click(x, y)

                if reset_easy_button.hover:
                    display_board.reset_to_original()

                if restart_medium_button.hover:
                    display_board = init_board()

                if exit_hard_button.hover:
                    running = False

            if event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()

                display_board.update_hover(x, y)

                reset_easy_button.update_hover(x, y)
                restart_medium_button.update_hover(x, y)
                exit_hard_button.update_hover(x, y)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    display_board.place_number(1)

                if event.key == pygame.K_2:
                    display_board.place_number(2)

                if event.key == pygame.K_3:
                    display_board.place_number(3)

                if event.key == pygame.K_4:
                    display_board.place_number(4)

                if event.key == pygame.K_5:
                    display_board.place_number(5)

                if event.key == pygame.K_6:
                    display_board.place_number(6)

                if event.key == pygame.K_7:
                    display_board.place_number(7)

                if event.key == pygame.K_8:
                    display_board.place_number(8)

                if event.key == pygame.K_9:
                    display_board.place_number(9)

                if event.key == pygame.K_BACKSPACE:
                    display_board.place_number(0)

        WINDOW.fill("white")

        WINDOW.blit(
            pygame.transform.scale(game_bg, (WINDOW.get_width(), WINDOW.get_height())),
            (0, 0),
        )

        display_board.draw()

        pygame.display.update()


def main():
    # Main Menu Loop

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()

                if reset_easy_button.hover:
                    Difficulty.set_difficulty(DifficultyLevel.EASY)
                    running = False

                if restart_medium_button.hover:
                    Difficulty.set_difficulty(DifficultyLevel.MEDIUM)
                    running = False

                if exit_hard_button.hover:
                    Difficulty.set_difficulty(DifficultyLevel.HARD)
                    running = False

            if event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()

                reset_easy_button.update_hover(x, y)
                restart_medium_button.update_hover(x, y)
                exit_hard_button.update_hover(x, y)

        WINDOW.fill("white")

        WINDOW.blit(
            pygame.transform.scale(
                main_menu_bg, (WINDOW.get_width(), WINDOW.get_height())
            ),
            (0, 0),
        )

        pygame.display.update()

    # Game Loop
    game_loop()


if __name__ == "__main__":
    main()
