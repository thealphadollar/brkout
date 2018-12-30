###############################################################
# Define your input scheme,
# Buttons and axis' here
#
# Guide for creating Buttons and Axis'
# Buttons:  first param is the name of the button, example:
#           reload, shoot etc.
#           second param is a list of pygame keycodes that
#           can be used for
#           that button, for example for reload, can use key
#           r or key 4
#           pressing key r or 4 will retun True
#           example use:
#           reload_game = input_manager.get_button('reload')
#
# Axis:     first param is the name of the Axis, example:
#           horizontal, vertical etc.
#           second param is a list of tuples. where the first
#           element of tuple is
#           the negative button and the second element is the
#           positive button.
#           for example, horizontal axis will have (key a, key d).
#           pressing key a will give -1, pressing key d will
#           give 1
#           example use:
#           move = input_manager.get_axis('horizontal')
##################################################################

from .input_button_down import Button_Down
from .input_button_up import Button_Up
from .input_button import Button
from .input_axis import Axis
import pygame.key


def get_input_list():
    input_list = dict()

    # reload
    input_list['reload'] = Button('reload', {pygame.K_r, pygame.K_4})

    # escape
    input_list['escape'] = Button_Up('escape', {pygame.K_SPACE, pygame.K_ESCAPE})

    # button up
    input_list['up'] = Button_Up('up', {pygame.K_w, pygame.K_UP})

    # button down
    input_list['down'] = Button_Up('down', {pygame.K_s, pygame.K_DOWN})

    # button right
    input_list['right'] = Button_Up('right', {pygame.K_d, pygame.K_RIGHT})

    # button left
    input_list['left'] = Button_Up('right', {pygame.K_a, pygame.K_LEFT})

    # enter
    input_list['enter'] = Button_Up('enter', {pygame.K_RETURN})

    # horizontal
    input_list['horizontal'] = Axis(
        'horizontal', {(pygame.K_a, pygame.K_d), (pygame.K_LEFT, pygame.K_RIGHT)})

    # vertical
    input_list['vertical'] = Axis(
        'vertical', {(pygame.K_s, pygame.K_w), (pygame.K_DOWN, pygame.K_UP)})

    return input_list
