# this file contains functions for global use
from constants import *
import random
import math

# function to render font


def text_obj(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()

# function to display text


def disp_text(screen, text, center, font_and_size, color):
    text_surf, text_rect = text_obj(text, font_and_size, color)
    text_rect.center = center
    screen.blit(text_surf, text_rect)

# function to draw walls around screen


def draw_walls(screen, brick_width, brick_height):

    # drawing rectangles
    initial_position_x = 0
    initial_position_y = 0

    # ceiling
    while initial_position_x <= (scr_width - wall_brick_width):
        pygame.draw.rect(screen, wall_orange, (initial_position_x,
                                               initial_position_y, brick_width, brick_height))
        initial_position_x += brick_width
        if not initial_position_x < scr_width:
            break
        pygame.draw.rect(screen, wall_silver, (initial_position_x,
                                               initial_position_y, brick_width, brick_height))
        initial_position_x += brick_width

    initial_position_x -= brick_height

    # right wall
    while initial_position_y <= (scr_height - brick_width):
        pygame.draw.rect(screen, wall_orange, (initial_position_x,
                                               initial_position_y, brick_height, brick_width))
        initial_position_y += brick_width
        if not initial_position_y < scr_height:
            break
        pygame.draw.rect(screen, wall_silver, (initial_position_x,
                                               initial_position_y, brick_height, brick_width))
        initial_position_y += brick_width

    initial_position_y -= brick_height
    initial_position_x += brick_height

    # floor
    while initial_position_x >= brick_width:
        initial_position_x -= brick_width
        pygame.draw.rect(screen, wall_orange, (initial_position_x,
                                               initial_position_y, brick_width, brick_height))
        if not initial_position_x > 0:
            break
        initial_position_x -= brick_width
        pygame.draw.rect(screen, wall_silver, (initial_position_x,
                                               initial_position_y, brick_width, brick_height))

    initial_position_y += brick_height

    # left wall
    while initial_position_y >= brick_width:
        initial_position_y -= brick_width
        pygame.draw.rect(screen, wall_orange, (initial_position_x,
                                               initial_position_y, brick_height, brick_width))
        if not initial_position_y > 0:
            break
        initial_position_y -= brick_width
        pygame.draw.rect(screen, wall_silver, (initial_position_x,
                                               initial_position_y, brick_height, brick_width))

    return


def draw_walls_white(screen, brick_width, brick_height):

    # drawing rectangles
    initial_position_x = 0
    initial_position_y = 0

    # ceiling
    while initial_position_x <= (scr_width - wall_brick_width):
        pygame.draw.rect(screen, white, (initial_position_x,
                                         initial_position_y, brick_width, brick_height))
        initial_position_x += brick_width
        if not initial_position_x < scr_width:
            break
        pygame.draw.rect(screen, white, (initial_position_x,
                                         initial_position_y, brick_width, brick_height))
        initial_position_x += brick_width

    initial_position_x -= brick_height

    # right wall
    while initial_position_y <= (scr_height - brick_width):
        pygame.draw.rect(screen, white, (initial_position_x,
                                         initial_position_y, brick_height, brick_width))
        initial_position_y += brick_width
        if not initial_position_y < scr_height:
            break
        pygame.draw.rect(screen, white, (initial_position_x,
                                         initial_position_y, brick_height, brick_width))
        initial_position_y += brick_width

    initial_position_y -= brick_height
    initial_position_x += brick_height

    # floor
    while initial_position_x >= brick_width:
        initial_position_x -= brick_width
        pygame.draw.rect(screen, white, (initial_position_x,
                                         initial_position_y, brick_width, brick_height))
        if not initial_position_x > 0:
            break
        initial_position_x -= brick_width
        pygame.draw.rect(screen, white, (initial_position_x,
                                         initial_position_y, brick_width, brick_height))

    initial_position_y += brick_height

    # left wall
    while initial_position_y >= brick_width:
        initial_position_y -= brick_width
        pygame.draw.rect(screen, white, (initial_position_x,
                                         initial_position_y, brick_height, brick_width))
        if not initial_position_y > 0:
            break
        initial_position_y -= brick_width
        pygame.draw.rect(screen, white, (initial_position_x,
                                         initial_position_y, brick_height, brick_width))

    return
