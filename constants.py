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
strike_bound_radius = 200
main_game_middle_x = 450
main_game_middle_y = 370
post_brick_width = 100
post_brick_height = 4

# striker constants
striker_radius = 40
striker_mass = 500
striker_friction = .1
MAX_STRIKER_SPEED = 15
striker_velocity = 0

# ball constants
ball_radius = 11
menu_ball_speed = 15
main_ball_speed = 0
MAX_BALL_SPEED = 10
ball_mass = 5
friction = .015

# text formats
game_title_text_large = pygame.font.Font(os.path.join(assets_directory, 'Weston Free.otf'), 120)
game_title_text_small = pygame.font.Font(os.path.join(assets_directory, 'Weston Free.otf'), 100)
menu_item_text_selected = pygame.font.Font(os.path.join(assets_directory, 'nougatine.ttf'), 35)
menu_item_text = pygame.font.Font(os.path.join(assets_directory, 'nougatine.ttf'), 30)
message_text = pygame.font.Font(os.path.join(assets_directory, 'ARCADECLASSIC.TTF'), 20)
credits_text = pygame.font.Font(os.path.join(assets_directory, 'SF Atarian System Extended Bold Italic.ttf'), 45)
credits_name = pygame.font.Font(os.path.join(assets_directory, 'Halo3.ttf'), 55)
main_screen_text = pygame.font.Font(os.path.join(assets_directory, 'FutureTimeSplittersupdate.otf'), 36)
main_screen_number = pygame.font.Font(os.path.join(assets_directory, 'digital-7.ttf'), 25)
pause_text = pygame.font.Font(os.path.join(assets_directory, 'chiller.ttf'), 50)
pause_text_s = pygame.font.Font(os.path.join(assets_directory, 'chiller.ttf'), 65)
end_screen_text = pygame.font.Font(os.path.join(assets_directory, 'FutureTimeSplittersupdate.otf'), 50)
end_screen_number = pygame.font.Font(os.path.join(assets_directory, 'digital-7.ttf'), 30)
end_title_text_win = pygame.font.Font(os.path.join(assets_directory, 'Jolly Bold.ttf'), 60)
end_title_text_lose = pygame.font.Font(os.path.join(assets_directory, 'PWScratchy.ttf'), 60)
quote_text = pygame.font.Font(os.path.join(assets_directory, 'TheHills.ttf'), 37)

# music files

# images
speed_red = pygame.image.load(os.path.join(assets_directory, 'speed_red.png'))
speed_blue = pygame.image.load(os.path.join(assets_directory, 'speed_blue.png'))

# colors
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
name_grey = (150, 150, 150)
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
pure_red = (255, 0, 0)
pure_green = (0, 255, 0)
pure_blue = (0, 0 , 255)
peace_green = (24, 163, 24)
blood_red = (138, 7, 7)
striker_colors = [green, red, magenta, blue]
brick_colors = [pure_green, pure_red, yellow]  # red are weakest, yellow are ok, and green are healthy
color_option_palette = [[green, light_green], [red, light_red], [magenta, light_magenta], [blue, light_blue]]
pause_col = grey
pause_sel_col = green

# hint messages
hint_message = ["Harder The Hit, Quicker Breaks The Brick", "Lesser The Hits, Higher The Score Picked", "Go For The \
Red, They Have Brittlest Head", "A Thumb Rule To Follow, Never Hit The Brick That Refuses To Glow", "More Time You \
Spend Behind Bars, Worse Are You, Once Out", "To A Patch You Are Bound, Since There's Light Around", "Thinking About \
Rest? Remember The Guards, Gathering Like It's A College Fest!"]