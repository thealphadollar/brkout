from __future__ import absolute_import
from __future__ import division

# function to set path to current folder (py 2 to 3)
from past.utils import old_div
def import_modify():
    if __name__ == '__main__':
        if __package__ is None:
            import sys
            from os import path
            sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))

try:
    from .start_screen import *
    from .global_funcs import *
    from .global_objects import *
    from .constants import *
except SystemError as er:
    from start_screen import *
    from global_funcs import *
    from global_objects import *
    from constants import *

import pygame
import os


def pause_game(screen, clock):

    # pauses music
    pygame.mixer.music.pause()

    # play pause screen music
    if mute:
        pause_sound.play(-1)
        pause_sound.set_volume(1)

    oldtime = pygame.time.get_ticks()
    pause_ball = Ball(130, 140)  # Initializing pause_ball
    option = 0
    # Giving a delay of 200 ms
    while pygame.time.get_ticks() - oldtime < 200:
        pass

    oldtime = pygame.time.get_ticks()
    while True:
        clock.tick(FPS)

        newtime = pygame.time.get_ticks()
        delta_time = old_div((newtime - oldtime),10)
        oldtime = newtime

        # checking events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os._exit(0)

            if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE):
                # unpause music
                pause_sound.stop()
                if mute:
                    pygame.mixer.music.unpause()
                return

            if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_w):
                option += 3
                option %= 4

            if event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                option += 1
                option %= 4

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                pause_sound.stop()
                if option != 3 and mute:
                    # unpause music
                    pygame.mixer.music.unpause()
                if option == 0:
                    return 0
                if option == 1:
                    return 1
                if option == 2:
                    return 2
                if option == 3:
                    os._exit(0)

        # ball updation
        pause_ball.menu_screen_move(delta_time)
        pause_ball.check_collide_wall()
        pause_ball.check_collide_options()

        # display update
        screen.fill(black)
        draw_walls(screen, 100, 30)
        # displaying the top text
        disp_text(screen, "Wait! I saw something", (old_div(scr_width, 2),
                                                    old_div(scr_height,2) - 250), pause_text_top, pause_text_tops)

        # displaying highlighted options
        if option == 0:
            disp_text(screen, "JUST A RAT!", (old_div(scr_width, 2),
                                              old_div(scr_height,2) - 100), pause_text_s, pause_sel_col)
            disp_text(screen, "PRESS ENTER TO RESUME", (old_div(scr_width,
                                                        2), scr_height - 50), message_text1, credit_orange)
        else:
            disp_text(screen, "JUST A RAT!", (old_div(scr_width, 2),
                                              old_div(scr_height,2) - 100), pause_text, pause_col)
        if option == 1:
            disp_text(screen, "YIKES! GUARDS", (old_div(scr_width, 2),
                                                old_div(scr_height,2) - 20), pause_text_s, pause_sel_col)
            disp_text(screen, "PRESS ENTER TO RESTART", (old_div(scr_width,
                                                         2), scr_height - 50), message_text1, credit_orange)
        else:
            disp_text(screen, "YIKES! GUARDS", (old_div(scr_width, 2),
                                                old_div(scr_height,2) - 20), pause_text, pause_col)
        if option == 2:
            disp_text(screen, "PRESS ENTER FOR MAIN MENU", (old_div(scr_width,
                                                            2), scr_height - 50), message_text1, credit_orange)
            disp_text(screen, "PULL OUT!", (old_div(scr_width, 2),
                                            old_div(scr_height,2) + 60), pause_text_s, pause_sel_col)
        else:
            disp_text(screen, "PULL OUT!", (old_div(scr_width, 2),
                                            old_div(scr_height,2) + 60), pause_text, pause_col)
        if option == 3:
            disp_text(screen, "PRESS ENTER TO QUIT", (old_div(scr_width, 2),
                                                      scr_height - 50), message_text1, credit_orange)
            disp_text(screen, "GIVE UP?", (old_div(scr_width, 2),
                                           old_div(scr_height,2) + 140), pause_text_s, pause_sel_col)
        else:
            disp_text(screen, "GIVE UP?", (old_div(scr_width, 2),
                                           old_div(scr_height,2) + 140), pause_text, pause_col)

        # drawing a box
        pygame.draw.rect(screen, white, (old_div(scr_width,2) - 170,
                                         old_div(scr_height,2) - 160, 340, 360), 2)
        pygame.draw.rect(screen, white, (old_div(scr_width,2) - 178,
                                         old_div(scr_height,2) - 168, 356, 376), 3)
        pygame.draw.aaline(screen, white, (old_div(scr_width,2) - 178, old_div(scr_height,
                                           2) - 168), (old_div(scr_width,2) + 178, old_div(scr_height,2) - 168), 1)
        pygame.draw.aaline(screen, white, (old_div(scr_width,2) - 178, old_div(scr_height,
                                           2) - 168), (old_div(scr_width,2) - 178, old_div(scr_height,2) + 208), 1)
        pygame.draw.aaline(screen, white, (old_div(scr_width,2) + 178, old_div(scr_height,
                                           2) + 208), (old_div(scr_width,2) - 178, old_div(scr_height,2) + 208), 1)
        pygame.draw.aaline(screen, white, (old_div(scr_width,2) + 178, old_div(scr_height,
                                           2) + 208), (old_div(scr_width,2) + 178, old_div(scr_height,2) - 168), 1)

        # draw ball
        pause_ball.draw(screen)
        pygame.display.update()
