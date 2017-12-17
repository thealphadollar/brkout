from global_funcs import *
from constants import *
from global_objects import Ball


# initiating the ball
menu_ball = Ball(scr_width/2, scr_height-wall_brick_height-ball_radius)


# function to draw walls around screen


def draw_walls(screen):

    # drawing rectangles
    initial_position_x = 0
    initial_position_y = 0

    # ceiling
    while initial_position_x <= (scr_width - wall_brick_width):
        pygame.draw.rect(screen, wall_orange, (initial_position_x, initial_position_y, wall_brick_width, wall_brick_height))
        initial_position_x += wall_brick_width
        if not initial_position_x < scr_width:
            break
        pygame.draw.rect(screen, wall_silver, (initial_position_x, initial_position_y, wall_brick_width, wall_brick_height))
        initial_position_x += wall_brick_width

    initial_position_x -= wall_brick_height

    # right wall
    while initial_position_y <= (scr_height - wall_brick_width):
        pygame.draw.rect(screen, wall_orange, (initial_position_x, initial_position_y, wall_brick_height, wall_brick_width))
        initial_position_y += wall_brick_width
        if not initial_position_y < scr_height:
            break
        pygame.draw.rect(screen, wall_silver, (initial_position_x, initial_position_y, wall_brick_height, wall_brick_width))
        initial_position_y += wall_brick_width

    initial_position_y -= wall_brick_height
    initial_position_x += wall_brick_height

    # floor
    while initial_position_x >= wall_brick_width:
        initial_position_x -= wall_brick_width
        pygame.draw.rect(screen, wall_orange, (initial_position_x, initial_position_y, wall_brick_width, wall_brick_height))
        if not initial_position_x > 0:
            break
        initial_position_x -= wall_brick_width
        pygame.draw.rect(screen, wall_silver, (initial_position_x, initial_position_y, wall_brick_width, wall_brick_height))

    initial_position_y += wall_brick_height

    # left wall
    while initial_position_y >= wall_brick_width:
        initial_position_y -= wall_brick_width
        pygame.draw.rect(screen, wall_orange, (initial_position_x, initial_position_y, wall_brick_height, wall_brick_width))
        if not initial_position_y > 0:
            break
        initial_position_y -= wall_brick_width
        pygame.draw.rect(screen, wall_silver, (initial_position_x, initial_position_y, wall_brick_height, wall_brick_width))

    return

# main function to display and handle menu screen


def menu_screen(screen, clock):

    # declaring important variables
    color_choice = 0
    option_flag = 0

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
        draw_walls(screen)

        # display moving ball
        menu_ball.menu_screen_move(delta_time)
        menu_ball.check_collide_wall()
        menu_ball.check_collide_palette()
        menu_ball.draw(screen)

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
        pygame.draw.rect(screen, white, (scr_width/2 - 200, scr_height/2 + 40, 400, 100), 2)

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
            disp_text(screen, "Press Enter To Quit", (scr_width / 2, scr_height / 2 + 300), message_text, yellow)

        pygame.display.update()
        clock.tick(60)
