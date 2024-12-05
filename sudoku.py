import pygame
from sudoku_generator import Cell, Board, generate_sudoku
from difficulty import Difficulty, DifficultyLevel
from button import get_buttons

# Initializng pygame font capabilities
pygame.font.init()

# Setting up global constants for later use
MAX_MISTAKES = 3
WINDOW_WIDTH = 590 * 1.5
WINDOW_HEIGHT = 410 * 1.5
BOARD_X = 10 * WINDOW_WIDTH / 590
BOARD_Y = 10 * WINDOW_HEIGHT / 410

# Setting up window/screen to display sudoku board on
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Setting title for the screen
pygame.display.set_caption("Smiski Sudoku")

# Setting up two fonts, one for the sudoku board and the other for ui such as the mistake counter
BOARD_FONT = pygame.font.SysFont(None, 20 if WINDOW_WIDTH <= 590 else 32)
UI_FONT = pygame.font.SysFont(None, 20 if WINDOW_WIDTH <= 590 else 32)

UI_FONT_COLOR = (248, 253, 232)
UI_FONT_OUTLINE_COLOR = (84, 118, 44)

# Setting up relative coordinates for mistake counter position and buttons
MISTAKE_X = 0.925 * WINDOW_WIDTH
MISTAKE_Y = 0.058 * WINDOW_HEIGHT

(reset_button, restart_button, exit_button, easy_button, medium_button, hard_button) = (
    get_buttons(WINDOW_WIDTH, WINDOW_HEIGHT)
)

# Setting up background images
main_menu_bg = pygame.image.load("assets/menu.webp").convert()
game_bg = pygame.image.load("assets/game.webp").convert()
won_bg = pygame.image.load("assets/won.webp").convert()
lost_bg = pygame.image.load("assets/lost.webp").convert()

Cell.init(BOARD_X, BOARD_Y, WINDOW, BOARD_FONT)


def draw_outlined_text(txt, x, y):
    thickness = 2

    WINDOW.blit(
        UI_FONT.render(txt, True, UI_FONT_OUTLINE_COLOR), (x - thickness, y - thickness)
    )

    WINDOW.blit(
        UI_FONT.render(txt, True, UI_FONT_OUTLINE_COLOR), (x + thickness, y - thickness)
    )

    WINDOW.blit(
        UI_FONT.render(txt, True, UI_FONT_OUTLINE_COLOR), (x - thickness, y + thickness)
    )

    WINDOW.blit(
        UI_FONT.render(txt, True, UI_FONT_OUTLINE_COLOR), (x + thickness, y + thickness)
    )

    WINDOW.blit(UI_FONT.render(txt, (x, y), UI_FONT_COLOR), (x, y))


def init_board() -> Board:
    """
        Initializes the sudoku board to be displayed and fills in the values according to the 
        SudokuGenerator generated board.

        Return: Board
    """
    
    sudoku_board = generate_sudoku(9, Difficulty.get_difficulty().value)
    display_board = Board(BOARD_X, BOARD_Y, 9, 9, WINDOW, BOARD_FONT, sudoku_board)

    return display_board


def status_loop(won=False):
    """
        Loop for rendering the status (game won/game lost) screen

        Note: exit_button could refer to either the restart or exit button based on whether the
        player won or lsot
    """

    # 0 -> Quit
    # 1 -> Restart/Exit
    state = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if exit_button.hover:
                    state = 1
                    running = False
            if event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()

                exit_button.update_hover(x, y)

        WINDOW.fill("white")

        WINDOW.blit(
            pygame.transform.scale(
                won_bg if won else lost_bg, (WINDOW.get_width(), WINDOW.get_height())
            ),
            (0, 0),
        )

        pygame.display.update()

    if state == 1 and not won:
        menu_loop()


def game_loop():
    """
        Loop for rendering the game screen with the sudoku board
    """
    
    display_board = init_board()

    mistakes = 0

    # 0 -> Quit
    # 1 -> Restart
    # 2 -> Lost
    # 3 -> Won
    state = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                x, y = pygame.mouse.get_pos()
                display_board.click(x, y)

                if reset_button.hover:
                    display_board.reset_to_original()
                    mistakes = 0

                if restart_button.hover:
                    state = 1
                    running = False

                if exit_button.hover:
                    state = 0
                    running = False
            if event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()

                display_board.update_hover(x, y)

                reset_button.update_hover(x, y)
                restart_button.update_hover(x, y)
                exit_button.update_hover(x, y)
            if event.type == pygame.KEYDOWN:
                if event.key >= pygame.K_1 and event.key <= pygame.K_9:
                    res = display_board.sketch(event.key - pygame.K_0)
                elif event.key == pygame.K_BACKSPACE:
                    display_board.sketch(0) # 0 -> erase
                elif event.key == pygame.K_RETURN:
                    res = display_board.place_number()
                    if res == -1: # incorrect value
                        mistakes += 1
                        if mistakes == MAX_MISTAKES:
                            state = 2
                            running = False
                    elif res == 1: # board is filled and correct
                        state = 3
                        running = False
                elif event.key == pygame.K_RIGHT:
                    display_board.move_selected((1, 0))
                elif event.key == pygame.K_LEFT:
                    display_board.move_selected((-1, 0))
                elif event.key == pygame.K_DOWN:
                    display_board.move_selected((0, 1))
                elif event.key == pygame.K_UP:
                    display_board.move_selected((0, -1))

        WINDOW.fill("white")

        WINDOW.blit(
            pygame.transform.scale(game_bg, (WINDOW.get_width(), WINDOW.get_height())),
            (0, 0),
        )

        draw_outlined_text(f"{mistakes}/{MAX_MISTAKES}", MISTAKE_X, MISTAKE_Y)

        display_board.draw()

        pygame.display.update()

    match state:
        case 1:
            menu_loop()
        case 2:
            status_loop(False)
        case 3:
            status_loop(True)


def menu_loop():
    """
        Loop for rendering the main menu/start screen
    """
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if easy_button.hover:
                    Difficulty.set_difficulty(DifficultyLevel.EASY)
                    running = False

                if medium_button.hover:
                    Difficulty.set_difficulty(DifficultyLevel.MEDIUM)
                    running = False

                if hard_button.hover:
                    Difficulty.set_difficulty(DifficultyLevel.HARD)
                    running = False

            if event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()

                easy_button.update_hover(x, y)
                medium_button.update_hover(x, y)
                hard_button.update_hover(x, y)

        # Default background color in case image doesn't load properly
        WINDOW.fill("white")

        # Transforms main menu background/buttons to fill the screen and then draws them
        WINDOW.blit(
            pygame.transform.scale(
                main_menu_bg, (WINDOW.get_width(), WINDOW.get_height())
            ),
            (0, 0),
        )

        pygame.display.update()

    # Game Loop
    game_loop()


def main():
    menu_loop()


if __name__ == "__main__":
    main()
