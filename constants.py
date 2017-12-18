# this file includes all the variables' initial value and constants.
import pygame
import os
pygame.init()

# asset directory
assets_directory = os.path.join(os.path.dirname(__file__), 'assets')

# brick constants
# horizontal brick
horizontal_brick_width = 70
horizontal_brick_height = 30
# vertical brick
vertical_brick_width = 35
vertical_brick_height = 60

# screen constants
FPS = 60
scr_width = 900
scr_height = 700
wall_brick_width = 100
wall_brick_height = 30
strike_bound_radius = 175
main_game_middle_x = 450
main_game_middle_y = 370

# striker constants
striker_radius = 50
striker_mass = 100
striker_friction = 0.5
MAX_STRIKER_SPEED = 7
striker_velocity = 0

# ball constants
ball_radius = 10
menu_ball_speed = 15
main_ball_speed = 20
MAX_BALL_SPEED = 22
ball_mass = 10
friction = .05

# text formats
game_title_text_large = pygame.font.Font(os.path.join(assets_directory, 'Weston Free.otf'), 120)
game_title_text_small = pygame.font.Font(os.path.join(assets_directory, 'Weston Free.otf'), 100)
menu_item_text_selected = pygame.font.Font(os.path.join(assets_directory, 'nougatine.ttf'), 35)
menu_item_text = pygame.font.Font(os.path.join(assets_directory, 'nougatine.ttf'), 30)
message_text = pygame.font.Font(os.path.join(assets_directory,'Calendas_Plus.otf'), 20)
credits_text = pygame.font.Font(pygame.font.match_font("chiller"),60)
credits_name = pygame.font.Font(pygame.font.match_font("Comic Sans MS"),35)
# music files

# images

# colors
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
light_black = (40, 40, 40)
wall_silver = (188, 198, 204)
silver = (192, 192, 192)
wall_orange = (212, 175, 55)
orange = (220, 126, 34)
yellow = (244, 208, 63)
green = (31, 181, 44)
light_green = (44, 222, 60)
red = (203, 67, 53)
light_red = (231, 76, 60)
magenta = (125, 60, 152)
light_magenta = (155, 89, 182)
blue = (46, 134, 193)
light_blue = (52, 152, 219)
credit_orange = (240, 146, 54)
pure_red = (255,0,0)
pure_green = (0,255,0)
striker_colors = [green, red, magenta, blue]
color_option_palette = [[green, light_green], [red, light_red], [magenta, light_magenta], [blue, light_blue]]
