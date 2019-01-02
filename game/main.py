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
from game.input_package.input_manager import *
        
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
    input_manager = Input_Manager()
    powerup_manager = Powerup_Manager(screen, 2, 160, 5, 5)
    game_manager = Game_Manager(
        pygame, screen, clock, settings_manager, sound_manager, animation_manager, game_parameters, input_manager, powerup_manager)

    return game_manager

def main():
    game_manager = init()

    # main menu game loop
    while True:
        main_menu_option, color_option, prison_option = menu_screen(game_manager)
        
        if main_menu_option == E_Main_Menu_Option.start_game:
            run_vars = Runtime_Vars()
            
            # game loop
            while True:
                game_output, run_vars = game_screen(game_manager, striker_colors[color_option.value], run_vars)

                if game_output is E_Game_Result.loss:
                    end_game_option = end_screen(game_manager, False, run_vars)

                elif game_output is E_Game_Result.win:
                    end_game_option = end_screen(game_manager, True, run_vars)
                
                elif game_output is E_Pause_Option.restart:
                    continue
                
                elif game_output is E_Pause_Option.main_menu:
                    break
                
                elif game_output is E_Pause_Option.quit:
                    os._exit(0)

                if end_game_option is E_End_Game_Option.restart:
                    continue
                
                elif end_game_option is E_End_Game_Option.main_menu:
                    break
                
                elif end_game_option is E_End_Game_Option.quit:
                    os._exit(0)

        elif main_menu_option is E_Main_Menu_Option.credits:
            credits_screen(game_manager)

        elif main_menu_option is E_Main_Menu_Option.quit:
            os._exit(0)
            

main()