import pygame
import os
import sys
import time
from global_funcs import *
from constants import *

# main function to display and handle menu screen


def menu_screen(screen, clock):

    # declaring important variables
    color_choice = 0
    option_flag = 0

    while True:

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
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(black)  # black background, to be changed later

        # display title
        disp_text(screen, "Brk", (scr_width/2 - 85, scr_height/2 - 200), game_title_text_large, orange)
        disp_text(screen, "OUT", (scr_width / 2 + 85, scr_height / 2 - 200), game_title_text_small, white)

        # display menu
        # display "Let's Play"
        if option_flag == 0:
            disp_text(screen, "Let's Escape", (scr_width/2, scr_height/2), menu_item_text_selected, silver)
        else:
            disp_text(screen, "Let's Escape", (scr_width/2, scr_height/2), menu_item_text, silver)

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
            disp_text(screen, "I'm Scared", (scr_width/2, scr_height/2 + 180), menu_item_text_selected, grey)
        else:
            disp_text(screen, "I'm Scared", (scr_width/2, scr_height/2 + 180), menu_item_text, grey)

        # display message
        if option_flag == 0:
            disp_text(screen, "Press Enter To Play", (scr_width/2, scr_height/2 + 300), message_text, yellow)
        elif option_flag == 1:
            disp_text(screen, "Press Enter To Exit", (scr_width / 2, scr_height / 2 + 300), message_text, yellow)
        pygame.display.update()
        clock.tick(10)
