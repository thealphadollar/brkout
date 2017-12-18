from start_screen import menu_screen
from global_funcs import *
from global_objects import *
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


# rendering static elements


def render_field():

    screen.fill(black)

    # drawing prison-field
    pygame.draw.rect(screen, grey, (100, 40, 700, 660))

    # drawing striker boundary
    pygame.draw.circle(screen, light_black, (main_game_middle_x, main_game_middle_y), strike_bound_radius)







# main game loop


def gameloop(striker_color):
    global screen, clock
    ball = Ball(main_game_middle_x, main_game_middle_y + strike_bound_radius)
    striker = Striker(main_game_middle_x, main_game_middle_y)
    first_strike = False

    while True:

        render_field()

        # getting in events
        for event in pygame.event.get():

            #updating striker with inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    striker.y_velocity += 3
                if event.key ==  pygame.K_DOWN:
                    striker.y_velocity -= 3
                if event.key == pygame.K_RIGHT:
                    striker.x_velocity += 3
                if event.key == pygame.K_LEFT:
                    striker.x_velocity -= 3

                # pausing the game
                if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                    #pause_game() function to add pause game
                    pass

            # quitting the game
            if event.type == pygame.QUIT:
                os._exit(0)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":

    while True:
        init()  # used to initialise the pygame module
        choice, color_choice = menu_screen(screen, clock)

        if choice == 0:
            gameloop(striker_colors[color_choice])
        elif choice == 1:
            os._exit(0)
