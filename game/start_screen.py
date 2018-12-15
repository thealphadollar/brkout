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
    from .global_funcs import *
    from .constants import *
    from .global_objects import Ball
    from .highscore import *
    from .settings_manager import Settings_Manager
    from .button import Button, ImgButton
    from .pygame_textinput import TextInput
except SystemError:
    from global_funcs import *
    from constants import *
    from global_objects import Ball
    from highscore import *
    from settings_manager import Settings_Manager
    from button import Button, ImgButton
    from pygame_textinput import TextInput


# initiating the ball
menu_ball = Ball(old_div(scr_width,2), scr_height-wall_brick_height-ball_radius)
first = 1
# main function to display and handle menu screen

def menu_screen(screen, clock):

    # declaring important variables
    color_choice = 0
    option_flag = 0
    prison_choice = 0
    random_hint = random.randint(0, 7)  # displays random quote
    high_score, high_time = read_highscore()
    timer = 0
    global mute, friction, first
    # playing start sound jail
    pygame.mixer.music.load(os.path.join(assets_directory, "start.wav"))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)

    # settings and player name
    settings_manager = Settings_Manager()
    is_editing_name = False
    edit_name_start_button = ImgButton(pygame, screen, (34, scr_height - 70, 32, 32), edit_start_img)
    edit_name_end_button = ImgButton(pygame, screen, (34, scr_height - 70, 32, 32), edit_end_img)
    name_input = TextInput('', text_color=(255, 255, 255), cursor_color=(255, 255, 255), font_and_size=message_text1)

    # display start image

    while timer <= 180 and first:
        timer += 1
        screen.blit(start_img_resized, (0, 0))
        draw_walls(screen, wall_brick_width, wall_brick_height)
        disp_text(screen, "Will You Make It Out... Alive?", (old_div(scr_width,2), 100), start_horror_text, peace_green)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os._exit(0)
        pygame.display.update()
        clock.tick(FPS)

    first = 0
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(assets_directory, "start_screen.ogg"))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(2)

    while True:

        if not mute:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        # time passed
        delta_time = old_div(clock.get_time(), 10)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # checking for events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    option_flag = (option_flag + 1) % 2
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    option_flag = (option_flag - 1) % 2
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    color_choice = (color_choice + 3) % 4
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    color_choice = (color_choice + 1) % 4
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    return option_flag, color_choice, mute  # return index of color in striker_colors

                if event.key == pygame.K_ESCAPE:
                    os._exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                if mouse_x < scr_width - 70 and mouse_x > scr_width -100 and mouse_y < 100 and mouse_y > 70 :
                    mute = not mute
                    mute = mute
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                if mouse_x < scr_width - 70 and mouse_x > scr_width -100 and mouse_y < 200 and mouse_y > 170 :
                    write_highscore(0,0,0,0,0)
                    high_score, high_time = read_highscore()
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                if mouse_x < 284 and mouse_x > 114 and mouse_y < 336 and mouse_y > 318 :
                    prison_choice = 0
                    friction = 0.01
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                if mouse_x < 527 and mouse_x > 325 and mouse_y < 336 and mouse_y > 318 :
                    prison_choice = 1
                    friction = 0.018
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                if mouse_x < 797 and mouse_x > 584 and mouse_y < 336 and mouse_y > 318 :
                    prison_choice = 2
                    friction = 0.025
            if event.type == pygame.QUIT:
                os._exit(0)

            # checking for button clicks
            if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                if is_editing_name:
                    if edit_name_end_button.check_click(event.pos):
                        settings_manager.settings_data['player_name'] = name_input.get_text()
                        settings_manager.save_settings_to_file()
                        is_editing_name = False
                else:
                    if edit_name_start_button.check_click(event.pos):
                        settings_manager.settings_data['player_name'] = ""
                        name_input.clear_text()
                        is_editing_name = True

            # fedd name input box with events
            name_input.update(events)

        screen.fill(black)  # black background, to be changed later
        draw_walls(screen, wall_brick_width, wall_brick_height)

        # display moving ball
        menu_ball.menu_screen_move(delta_time)
        menu_ball.check_collide_wall()
        menu_ball.check_collide_palette()
        menu_ball.draw(screen)

        # display quote
        # displaying random hint
        disp_text(screen, "\"" + hint_message[random_hint % 7] + "\"", (old_div(scr_width, 2), old_div(scr_height, 4) + 20),
                  quote_text, orange)

        # display title
        disp_text(screen, "Brk", (old_div(scr_width,2) - 70, old_div(scr_height,
                                  2) - 240), game_title_text_large, orange)
        disp_text(screen, "OUT", (old_div(scr_width, 2) + 100, old_div(scr_height,
                                  2) - 240), game_title_text_small, white)

        disp_text(screen, "YOUR PRISON", (old_div(scr_width, 2), old_div(scr_height,
                                  2) - 80), prison_text_big, blood_red)

        if prison_choice == 0:
            disp_text(screen, "HOME", (old_div(scr_width, 2) -250, old_div(scr_height,
                                    2) - 24), prison_text1, blue)
        else :
            disp_text(screen, "HOME", (old_div(scr_width, 2) -250, old_div(scr_height,
                                    2) - 24), prison_text, yellow)

        if prison_choice == 1:
            disp_text(screen, "DUNGEON", (old_div(scr_width, 2) - 25, old_div(scr_height,
                                    2) - 24), prison_text1, blue)
        else :
            disp_text(screen, "DUNGEON", (old_div(scr_width, 2) - 25, old_div(scr_height,
                                    2) - 24), prison_text, yellow)

        if prison_choice == 2:
            disp_text(screen, "TARTARUS", (old_div(scr_width, 2) + 240, old_div(scr_height,
                                    2) - 24), prison_text1, blue)
        else :
            disp_text(screen, "TARTARUS", (old_div(scr_width, 2) + 240, old_div(scr_height,
                                    2) - 24), prison_text, yellow)

        disp_text(screen, "HIGHSCORE", (130, 65), start_screen_number, white)
        disp_text(screen, high_score , (130, 105), start_screen_number1, white)
        disp_text(screen, high_time[:2] + ":" + high_time[2:4] , (130, 140), start_screen_number1, white)

        if mute:
            screen.blit(unmute_img,(scr_width - 100,70))
        else:
            screen.blit(mute_img,(scr_width - 100,70))
        screen.blit(help_img,(scr_width - 100,120))
        screen.blit(reset_img,(scr_width - 100,170))
        # display menu
        # display "Let's Play"
        if option_flag == 0:
            disp_text(screen, "Let's Escape", (old_div(scr_width,2),
                                               old_div(scr_height,2) + 60), menu_item_text_selected, silver)
        else:
            disp_text(screen, "Let's Escape", (old_div(scr_width,2),
                                               old_div(scr_height,2) + 60), menu_item_text, grey)

        # display white boundary around color palette
        pygame.draw.rect(screen, white, (old_div(scr_width,2) - 200,
                                         old_div(scr_height,2) + 100, 400, 100), 3)
        pygame.draw.rect(screen, white, (old_div(scr_width, 2) - 192,
                                         old_div(scr_height, 2) + 108, 384, 84), 2)

        # display color palette
        if color_choice == 0:
            pygame.draw.rect(screen, light_green,
                             (old_div(scr_width,2) - 190, old_div(scr_height,2) + 110, 80, 80))
        else:
            pygame.draw.rect(screen, green, (old_div(scr_width, 2) -
                                             185, old_div(scr_height, 2) + 115, 70, 70))

        if color_choice == 1:
            pygame.draw.rect(screen, light_red, (old_div(scr_width,
                                                 2) - 90, old_div(scr_height,2) + 110, 80, 80))
        else:
            pygame.draw.rect(screen, red, (old_div(scr_width,2) - 85,
                                           old_div(scr_height, 2) + 115, 70, 70))

        if color_choice == 2:
            pygame.draw.rect(screen, light_magenta,
                             (old_div(scr_width,2) + 10, old_div(scr_height,2) + 110, 80, 80))
        else:
            pygame.draw.rect(screen, magenta, (old_div(scr_width,
                                               2) + 15, old_div(scr_height, 2) + 115, 70, 70))

        if color_choice == 3:
            pygame.draw.rect(screen, light_blue, (old_div(scr_width,
                                                  2) + 110, old_div(scr_height,2) + 110, 80, 80))
        else:
            pygame.draw.rect(screen, blue, (old_div(scr_width, 2) +
                                            115, old_div(scr_height, 2) + 115, 70, 70))

        # display "I'm Scared"
        if option_flag == 1:
            disp_text(screen, "I'm Scared", (old_div(scr_width,2), old_div(scr_height,
                                             2) + 240), menu_item_text_selected, silver)
        else:
            disp_text(screen, "I'm Scared", (old_div(scr_width,2),
                                             old_div(scr_height,2) + 240), menu_item_text, grey)

        # display message
        if mouse_x < scr_width - 70 and mouse_x > scr_width -100 and mouse_y < 100 and mouse_y > 70 :
            if mute:
                disp_text(screen, "Click To Mute", (old_div(scr_width,
                                                        2), old_div(scr_height,2) + 300), message_text, yellow)
            else :
                disp_text(screen, "Click To Unmute", (old_div(scr_width,
                                                        2), old_div(scr_height,2) + 300), message_text, yellow)
        elif mouse_x < scr_width - 70 and mouse_x > scr_width - 100 and mouse_y < 150 and mouse_y > 120 :
            disp_text(screen, "Click For Help", (old_div(scr_width,
                                                      2), old_div(scr_height,2) + 300), message_text, yellow)
        elif mouse_x < scr_width - 70 and mouse_x > scr_width - 100 and mouse_y < 200 and mouse_y > 170 :
            disp_text(screen, "Click To Reset Highscore", (old_div(scr_width,
                                                      2), old_div(scr_height,2) + 300), message_text, yellow)
        elif option_flag == 0:
            disp_text(screen, "Press Enter To Play", (old_div(scr_width,
                                                      2), old_div(scr_height,2) + 300), message_text, yellow)
        elif option_flag == 1:
            disp_text(screen, "Press Enter To Quit Game", (old_div(scr_width,
                                                           2), old_div(scr_height, 2) + 300), message_text, yellow)

        # display player name
        disp_text_origin(screen, settings_manager.settings_data['player_name'], (80, scr_height - 70), message_text1, white, )
        if is_editing_name:
            edit_name_end_button.draw()
        else:
            edit_name_start_button.draw()

        if is_editing_name:
            screen.blit(name_input.get_surface(), (80, scr_height - 70))

        

        pygame.display.update()
        clock.tick(FPS)
