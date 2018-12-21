from __future__ import absolute_import
from __future__ import division

# Setting path to current folder
from builtins import str
from past.utils import old_div
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))
import os
from game.global_objects import *
from game.screens import *
from game.animation_package import *
from game.objects import *
from game.misc import *
        
# function to initialise pygame

def init():
    pygame.init()

    gamelogo = pygame.image.load(os.path.join(assets_directory, 'logo.png'))
    pygame.display.set_icon(gamelogo)
    pygame.display.set_caption("BrkOut")
    screen = pygame.display.set_mode((scr_width, scr_height))
    clock = pygame.time.Clock()

    settings_manager = Settings_Manager()
    sound_manager = Sound_Manager(settings_manager, pygame)
    animation_manager = Animation_Manager(screen)
    game_parameters = Game_Parameters()
    game_manager = Game_Manager(pygame, screen, clock, settings_manager, sound_manager, animation_manager, game_parameters)

    return game_manager

def main():
    game_manager = init()

    while True:
        main_menu_option, color_option, prison_option = menu_screen(game_manager)

        # if the player presses "Let's Escape"
        if main_menu_option == E_Main_Menu_Option.start_game:
            end_choice = game_screen(game_manager, striker_colors[color_option.value])
            # As long as player presses restart
            first = True
            while end_choice == 2 or first:
                if not first:
                    init()
                    end_choice = gameloop(striker_colors[color_choice])

                # if the player looses
                if end_choice == 0:
                    end_choice = end_screen(
                        screen, False, score, seconds_first, seconds_second, minutes_first, minutes_second, clock, busts, escapes, mute)

                # if the player wins
                elif end_choice == 1:
                    end_choice = end_screen(

                        screen, True, score, seconds_first, seconds_second, minutes_first, minutes_second, clock, busts, escapes, mute)


                first = False

            # if the player presses "Main Menu", loop goes on!

        # if the player presses "I m scared"
        elif choice == 1:
            credits_screen(screen, clock)
main()