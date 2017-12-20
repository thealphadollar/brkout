from global_funcs import *
from constants import *
from global_objects import Ball


# initiating the ball
menu_ball = Ball(scr_width/2, scr_height-wall_brick_height-ball_radius)

# main function to display and handle menu screen


def menu_screen(screen, clock):

    # declaring important variables
    color_choice = 0
    option_flag = 0
    random_hint = random.randint(0, 7)  # displays random quote

    while True:

        # time passed
        delta_time = clock.get_time() / 10

        # checking for events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    option_flag = (option_flag + 1) % 2
                if event.key == pygame.K_DOWN:
                    option_flag = (option_flag - 1) % 2
                if event.key == pygame.K_LEFT:
                    color_choice = (color_choice + 3) % 4
                if event.key == pygame.K_RIGHT:
                    color_choice = (color_choice + 1) % 4
                if event.key == pygame.K_RETURN:
                    return option_flag, color_choice  # return index of color in striker_colors

                if event.key == pygame.K_ESCAPE:
                    print("I'm here")
                    os._exit(0)
            if event.type == pygame.QUIT:
                os._exit(0)

        screen.fill(black)  # black background, to be changed later
        draw_walls(screen, wall_brick_width, wall_brick_height)

        # display moving ball
        menu_ball.menu_screen_move(delta_time)
        menu_ball.check_collide_wall()
        menu_ball.check_collide_palette()
        menu_ball.draw(screen)

        # display quote
        # displaying random hint
        disp_text(screen, "\"" + hint_message[random_hint % 7] + "\"", (scr_width / 2, scr_height / 4 + 100),
                  quote_text, orange)

        # display title
        disp_text(screen, "Brk", (scr_width/2 - 85, scr_height/2 - 200), game_title_text_large, orange)
        disp_text(screen, "OUT", (scr_width / 2 + 85, scr_height / 2 - 200), game_title_text_small, white)

        # display menu
        # display "Let's Play"
        if option_flag == 0:
            disp_text(screen, "Let's Escape", (scr_width/2, scr_height/2), menu_item_text_selected, silver)
        else:
            disp_text(screen, "Let's Escape", (scr_width/2, scr_height/2), menu_item_text, grey)

        # display white boundary around color palette
        pygame.draw.rect(screen, white, (scr_width/2 - 200, scr_height/2 + 40, 400, 100), 3)
        pygame.draw.rect(screen, white, (scr_width / 2 - 192, scr_height / 2 + 48, 384, 84), 2)

        # display color palette
        if color_choice == 0:
            pygame.draw.rect(screen, light_green, (scr_width/2 - 190, scr_height/2 + 50, 80, 80))
        else:
            pygame.draw.rect(screen, green, (scr_width / 2 - 185, scr_height / 2 + 55, 70, 70))

        if color_choice == 1:
            pygame.draw.rect(screen, light_red, (scr_width/2 - 90, scr_height/2 + 50, 80, 80))
        else:
            pygame.draw.rect(screen, red, (scr_width/2 - 85, scr_height / 2 + 55, 70, 70))

        if color_choice == 2:
            pygame.draw.rect(screen, light_magenta, (scr_width/2 + 10, scr_height/2 + 50, 80, 80))
        else:
            pygame.draw.rect(screen, magenta, (scr_width / 2 + 15, scr_height / 2 + 55, 70, 70))

        if color_choice == 3:
            pygame.draw.rect(screen, light_blue, (scr_width/2 + 110, scr_height/2 + 50, 80, 80))
        else:
            pygame.draw.rect(screen, blue, (scr_width / 2 + 115, scr_height / 2 + 55, 70, 70))

        # display "I'm Scared"
        if option_flag == 1:
            disp_text(screen, "I'm Scared", (scr_width/2, scr_height/2 + 180), menu_item_text_selected, silver)
        else:
            disp_text(screen, "I'm Scared", (scr_width/2, scr_height/2 + 180), menu_item_text, grey)

        # display message
        if option_flag == 0:
            disp_text(screen, "Press Enter To Play", (scr_width/2, scr_height/2 + 300), message_text, yellow)
        elif option_flag == 1:
            disp_text(screen, "Press Enter To Quit Game", (scr_width / 2, scr_height / 2 + 300), message_text, yellow)

        pygame.display.update()
        clock.tick(FPS)
