import pygame


class Button:
    def __init__(self, rect: pygame.Rect):
        self.rect = rect
        self.hover = False

    
    def update_hover(self, x: int, y: int):
        """
            Updates whether the buttons is being hovered over by the mouse or not

            Parameters:
            x and y are the mouse coordinates
        """
        if self.rect.collidepoint(x, y):
            if not self.hover:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            self.hover = True
        else:
            if self.hover:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            self.hover = False


def get_buttons(width: float, height: float):
    """
        Sets up buttons (extension of pygame rects) using relative positions and sizes for responsiveness
    """

    BUTTON_WIDTH = 0.135 * width
    BUTTON_HEIGHT = 0.09 * height

    RESET_BUTTON_X = 0.715 * width
    RESET_BUTTON_Y = 0.125 * height 

    RESTART_BUTTON_X = 0.858 * width 
    RESTART_BUTTON_Y = 0.125 * height

    EXIT_BUTTON_X = 0.775 * width
    EXIT_BUTTON_Y = 0.223 * height

    EASY_BUTTON_X = 0.695 * width
    EASY_BUTTON_Y = 0.05 * height

    MEDIUM_BUTTON_X = 0.85 * width
    MEDIUM_BUTTON_Y = 0.05 * height

    HARD_BUTTON_X = 0.773 * width
    HARD_BUTTON_Y = 0.163 * height

    reset_button = Button(
        pygame.Rect(RESET_BUTTON_X, RESET_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
    )

    restart_button = Button(
        pygame.Rect(RESTART_BUTTON_X, RESTART_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
    )

    exit_button = Button(
        pygame.Rect(EXIT_BUTTON_X, EXIT_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
    )

    easy_button = Button(
        pygame.Rect(EASY_BUTTON_X, EASY_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
    )

    medium_button = Button(
        pygame.Rect(MEDIUM_BUTTON_X, MEDIUM_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
    )

    hard_button = Button(
        pygame.Rect(HARD_BUTTON_X, HARD_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
    )

    return (
        reset_button,
        restart_button,
        exit_button,
        easy_button,
        medium_button,
        hard_button,
    )
