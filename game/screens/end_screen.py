from __future__ import absolute_import
from __future__ import division

# function to set path to current folder (py 2 to 3)
from builtins import str
from past.utils import old_div


def import_modify():
    if __name__ == '__main__':
        if __package__ is None:
            import sys
            from os import path
            sys.path.append(path.abspath(
                path.join(path.dirname(__file__), '..')))


try:
    from game.global_objects import *
    from game.misc import *
    from game.objects.ball import Ball
except SystemError:
    from .global_objects import *
    from .misc import *
    from .objects.ball import Ball


def end_screen(game_manager, win, run_vars):
    pygame = game_manager.pygame
    screen = game_manager.screen
    clock = game_manager.clock
    sound_manager = game_manager.sound_manager
    score = run_vars.score
    seconds_first = run_vars.seconds_first
    seconds_second = run_vars.seconds_second
    minutes_first = run_vars.minutes_first
    minutes_second = run_vars.minutes_second
    busts = run_vars.busts
    escapes = run_vars.escapes
    end_game_option = E_End_Game_Option.restart

    if win:
        sound_manager.play_music('victory.ogg')
    else:
        sound_manager.play_music('end_loss.mp3')

    # initialising ball for this screen
    ball = Ball(old_div(scr_width, 2), scr_height - wall_brick_height)
    new_high, new_time = read_highscore()
    new_high = int(new_high)
    if new_high < score:
        write_highscore(score, minutes_second, minutes_first,
                        seconds_second, seconds_first)

    random_hint = random.randint(0, 7)  # getting value for random hint
    while True:

        # time passed
        delta_time = old_div(clock.get_time(), 10)

        # if player won the game, theme like he is out of the captivity
        if win:
            screen.fill(white)
            disp_text(screen, "Sweet Open Air!", (old_div(scr_width, 2), old_div(scr_height, 4)), end_title_text_win,
                      peace_green)
            # displaying menu options
            if end_game_option is E_End_Game_Option.restart:
                disp_text(screen, "Get Dirty Again", (old_div(scr_width, 2),
                                                      old_div(scr_height, 2) + 80), menu_item_text_selected, black)
            else:
                disp_text(screen, "Get Dirty Again", (old_div(scr_width, 2),
                                                      old_div(scr_height, 2) + 80), menu_item_text, light_black)

            if end_game_option is E_End_Game_Option.main_menu:
                disp_text(screen, "Rest A While", (old_div(scr_width, 2),
                                                   old_div(scr_height, 2) + 130), menu_item_text_selected, black)
            else:
                disp_text(screen, "Rest A While", (old_div(scr_width, 2),
                                                   old_div(scr_height, 2) + 130), menu_item_text, light_black)

            if end_game_option is E_End_Game_Option.quit:
                disp_text(screen, "Food Stinks There!", (old_div(scr_width, 2),
                                                         old_div(scr_height, 2) + 180), menu_item_text_selected, black)
            else:
                disp_text(screen, "Food Stinks There!", (old_div(scr_width, 2),
                                                         old_div(scr_height, 2) + 180), menu_item_text, light_black)

            # drawing box around options
            pygame.draw.rect(screen, black, (old_div(scr_width, 2)
                                             - 250, old_div(scr_height, 2) + 40, 500, 190), 2)
            pygame.draw.rect(screen, black, (old_div(scr_width, 2)
                                             - 242, old_div(scr_height, 2) + 48, 484, 174), 2)

        # if player caught
        else:
            screen.fill(black)
            draw_walls(screen, wall_brick_width, wall_brick_height)
            disp_text(screen, "Dragged Behind Bars!!", (old_div(scr_width, 2),
                                                        old_div(scr_height, 4)), end_title_text_lose, blood_red)

            # ball updates
            ball.menu_screen_move(delta_time)
            ball.check_collide_lose()
            ball.check_collide_wall()
            ball.draw(screen)

            # displaying menu options
            if end_game_option is E_End_Game_Option.restart:
                disp_text(screen, "Pull It Again", (old_div(scr_width, 2),
                                                    old_div(scr_height, 2) + 80), menu_item_text_selected, silver)
            else:
                disp_text(screen, "Pull It Again", (old_div(scr_width, 2),
                                                    old_div(scr_height, 2) + 80), menu_item_text, grey)

            if end_game_option is E_End_Game_Option.main_menu:
                disp_text(screen, "Change Disguise", (old_div(scr_width, 2),
                                                      old_div(scr_height, 2) + 130), menu_item_text_selected, silver)
            else:
                disp_text(screen, "Change Disguise", (old_div(scr_width, 2),
                                                      old_div(scr_height, 2) + 130), menu_item_text, grey)

            if end_game_option is E_End_Game_Option.quit:
                disp_text(screen, "Give Up?", (old_div(scr_width, 2),
                                               old_div(scr_height, 2) + 180), menu_item_text_selected, silver)
            else:
                disp_text(screen, "Give Up?", (old_div(scr_width, 2),
                                               old_div(scr_height, 2) + 180), menu_item_text, grey)

            # drawing box around options
            pygame.draw.rect(screen, white, (old_div(scr_width, 2)
                                             - 250, old_div(scr_height, 2) + 40, 500, 190), 3)
            pygame.draw.rect(screen, white, (old_div(scr_width, 2)
                                             - 242, old_div(scr_height, 2) + 48, 484, 174), 2)

        # display score
        disp_text(screen, "score : ", (old_div(scr_width, 4) - 65,
                                       old_div(scr_height, 8) - 30), end_screen_text, grey)
        disp_text(screen, str(score), (old_div(scr_width, 4), old_div(scr_height,
                                                                      8) + 2 - 30), end_screen_number, light_green)
        # display busts
        disp_text(screen, "busts : ", (scr_width / 2 - 105,
                                       scr_height / 8 - 30), end_screen_text, grey)
        disp_text(screen, str(busts), (scr_width / 2 - 45, scr_height
                                       / 8 + 2 - 30), end_screen_number, light_green)
        # display escapes
        disp_text(screen, "escapes : ", (scr_width / 2 + 65,
                                         scr_height / 8 - 30), end_screen_text, grey)
        disp_text(screen, str(escapes), (scr_width / 2 + 130, scr_height /
                                         8 + 2 - 30), end_screen_number, light_green)

        # display time
        disp_text(screen, "pursuit : ", (3 * scr_width / 4,
                                         old_div(scr_height, 8) - 30), end_screen_text, grey)
        disp_text(screen, str(minutes_second) + str(minutes_first) + ":" + str(seconds_second) + str(seconds_first),
                  (3 * scr_width / 4 + 85, old_div(scr_height, 8) + 2 - 30), end_screen_number, light_red)

        # display message
        if end_game_option is E_End_Game_Option.restart:
            disp_text(screen, "Press Enter To Restart",
                      (old_div(scr_width, 2), old_div(scr_height, 2) + 300), message_text, red)
        elif end_game_option is E_End_Game_Option.main_menu:
            disp_text(screen, "Press Enter To Go To Menu",
                      (old_div(scr_width, 2), old_div(scr_height, 2) + 300), message_text, red)
        elif end_game_option is E_End_Game_Option.quit:
            disp_text(screen, "Press Enter To Quit Game",
                      (old_div(scr_width, 2), old_div(scr_height, 2) + 300), message_text, red)

        # displaying random hint
        disp_text(screen, "\"" + hint_message[random_hint % 7] + "\"",
                  (old_div(scr_width, 2), old_div(scr_height, 4) + 100), quote_text, orange)

        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 and (pressed[pygame.K_RALT] or pressed[pygame.K_LALT]):
                    os._exit(0)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_d:
                    end_game_option = increase_enum(end_game_option)
                if event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_a:
                    end_game_option = decrease_enum(end_game_option)
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    return end_game_option
            if event.type == pygame.QUIT:
                os._exit(0)

        pygame.display.update()
        clock.tick(FPS)
