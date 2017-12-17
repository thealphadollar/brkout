from start_screen import menu_screen
from global_funcs import *
from constants import *
import os
import time

# function to initialise pygame


def init():

    global screen, clock

    # initialising sound system
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.init()

    # initialising display
    gamelogo = pygame.image.load(os.path.join(assets_directory, 'logo.png'))
    pygame.display.set_icon(gamelogo)
    pygame.display.set_caption("BrkOut")
    screen = pygame.display.set_mode((scr_width, scr_height))

    # initialising time
    clock = pygame.time.Clock()


if __name__ == "__main__":

    while True:
        init()  # used to initialise the pygame module
        choice, color_choice = menu_screen(screen, clock)

        if choice == 0:
            gameloop(color_choice)
        elif choice == 1:
            os._exit(0)
