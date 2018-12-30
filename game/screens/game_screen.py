from __future__ import absolute_import
from __future__ import division
from past.utils import old_div

# function to set path to current folder (py 2 to 3)


def import_modify():
    if __name__ == '__main__':
        if __package__ is None:
            import sys
            from os import path
            sys.path.append(path.abspath(
                path.join(path.dirname(__file__), '..')))


try:
    from game.objects import *
    from game.global_objects import *
    from game.gui_package import *
    from game.misc import *
    from game.screens.pause_screen import *
except SystemError:
    from .objects import *
    from .global_objects import *
    from .gui_package import *
    from .misc import *
    from .screens.pause_screen import *


class Runtime_Vars():
    def __init__(self):
        self.hit_count = 0  # stores number of bricks hit
        self.brick_point = 0  # stores the score accumulated by hitting brick
        self.score_time = 0  # timer for the score calculation
        self.time_count = 0  # increases score_time after 60 frames
        self.count_to_seconds = 0
        self.seconds_first = 0
        self.minutes_first = 0
        self.minutes_second = 0
        self.seconds_second = 0
        self.score = 0
        self.flip_image = 0
        self.pause_option = E_Pause_Option.resume
        self.escapes = 0
        self.busts = 0

    def reset(self):
        ''' If restarting a game, reset everthing at the start of a run, 
            except escapes and busts. 
        '''
        self.hit_count = 0
        self.brick_point = 0
        self.score_time = 0
        self.time_count = 0
        self.count_to_seconds = 0
        self.seconds_first = 0
        self.minutes_first = 0
        self.minutes_second = 0
        self.seconds_second = 0
        self.score = 0
        self.flip_image = 0
        self.pause_option = E_Pause_Option.resume


def game_screen(game_manager, striker_color, previous_run_vars):
    pygame = game_manager.pygame
    screen = game_manager.screen
    clock = game_manager.clock
    animation_manager = game_manager.animation_manager
    animation_manager.remove_all_animations()
    sound_manager = game_manager.sound_manager
    ball = Ball(main_game_middle_x + 50,
                main_game_middle_y + strike_bound_radius - 75)
    striker = Striker(main_game_middle_x, main_game_middle_y)

    run_vars = previous_run_vars
    run_vars.reset()

    sound_manager.play_music('main_music.mp3')

    game_area_collider = Rect_Collider(
        scr_width // 2, scr_height // 2 + 40, scr_width - 200, scr_height - 40)

    bricks = pygame.sprite.Group()
    add_to_group(bricks)

    start_timer = False

    while True:
        # time passed
        delta_time = old_div(clock.get_time(), 10)

        # drawing the game field
        render_field(pygame, screen, run_vars)

        # getting the events
        events(game_manager, pygame, screen,
               clock, striker, run_vars)

        # returning pause options if it is not resume
        if run_vars.pause_option is not E_Pause_Option.resume:
            return run_vars.pause_option, run_vars

        # updating elements
        striker.update(delta_time)
        ball.main_screen_move(delta_time)
        striker.check_bound()

        # checking collisions
        check_collisions(ball, bricks, run_vars,
                         animation_manager, sound_manager, delta_time)

        # check first strike to start timer
        if not start_timer:
            start_timer = ball.collision_striker(striker)
        else:
            if ball.collision_striker(striker):
                pass

        # checking winning
        if ball.check_escape(game_area_collider):
            temp_time = pygame.time.get_ticks()
            run_vars.escapes += 1
            while pygame.time.get_ticks() - temp_time < 400:
                pass
            return E_Game_Result.win, run_vars

        # rendering various elements
        striker.draw(screen, striker_color)
        ball.draw(screen)

        # drawing bricks
        for br in bricks:
            br.draw(screen)

        # show time function
        show_time(start_timer, screen, run_vars)

        # show score
        show_score(start_timer, screen, run_vars)

        # show speed
        show_speed(screen, ball)

        # check loosing
        if ball.speed == 0 and start_timer:
            temp_time = pygame.time.get_ticks()
            run_vars.busts += 1
            while pygame.time.get_ticks() - temp_time < 400:
                pass
            return E_Game_Result.loss, run_vars

        # draw animations
        animation_manager.draw_animations()

        # flipping
        pygame.display.update()
        clock.tick(FPS)


def add_to_group(bricks):
    y = 0
    while y < 4:
        x = 100 + y * vertical_brick_width
        while x < 800 - y * vertical_brick_width:
            b = Bricks(x, 40 + y * horizontal_brick_height, 1)
            bricks.add(b)
            x += horizontal_brick_width
        y += 1
    y = 0
    while y < 4:
        x = 100 + y * vertical_brick_width
        while x < 800 - y * vertical_brick_width:
            b = Bricks(x, 670 - y * horizontal_brick_height, 1)
            bricks.add(b)
            x += horizontal_brick_width
        y += 1
    x = 1
    while x < 5:
        y = 40 + x * horizontal_brick_height
        while y < 700 - x * horizontal_brick_height:
            b = Bricks(100 + (x - 1) * vertical_brick_width, y, 0)
            bricks.add(b)
            y += vertical_brick_height
        x += 1

    x = 1
    while x < 5:
        y = 40 + x * horizontal_brick_height
        while y < 700 - x * horizontal_brick_height:
            b = Bricks(800 - x * vertical_brick_width, y, 0)
            bricks.add(b)
            y += vertical_brick_height
        x += 1


def show_time(start_timer, screen, run_vars):
    if start_timer:
        run_vars.count_to_seconds += 1

    if run_vars.count_to_seconds == FPS:
        run_vars.seconds_first += 1
        run_vars.count_to_seconds = 0
    if run_vars.seconds_first == 10:
        run_vars.seconds_second += 1
        run_vars.seconds_first = 0
    if run_vars.seconds_second == 6:
        run_vars.minutes_first += 1
        run_vars.seconds_second = 0
    if run_vars.minutes_first == 10:
        run_vars.minutes_second += 1
        run_vars.minutes_first = 0

    # displaying time label
    disp_text(screen, "pursuit : ", (scr_width - 110, 21),
              main_screen_text, silver)
    disp_text(screen, str(run_vars.minutes_second) + str(run_vars.minutes_first) + ":" + str(run_vars.seconds_second) + str(run_vars.seconds_first),
              (scr_width - 40, 21), main_screen_number, silver)


def show_score(start_timer, screen, run_vars):
    # keeping track of time for scoring
    if start_timer:
        run_vars.time_count += 1

    # updating score variable
    if run_vars.time_count == 60:
        run_vars.score_time += 1
        run_vars.time_count = 0

    if run_vars.score_time > 0:
        run_vars.score = int(
            old_div(run_vars.brick_point, (.7 * math.sqrt(run_vars.score_time) + .3 * (run_vars.hit_count ** (old_div(1.0, 3))))))

    # negative score not allowed
    if run_vars.score < 0:
        run_vars.score = 0

    # method same as show_time to be adopted for displaying

    # displaying score label
    disp_text(screen, "score : ", (50, 21), main_screen_text, silver)
    disp_text(screen, str(run_vars.score),
              (100, 21), main_screen_number, silver)


def show_speed(screen, ball):

    disp_text(screen, "speed :", (old_div(scr_width, 2) - 30, 21),
              main_screen_text, silver)
    if (ball.speed * 10) > 70:
        disp_text(screen, str(int(ball.speed * 10)),
                  (old_div(scr_width, 2) + 15, 21), main_screen_number, pure_green)
    elif (ball.speed * 10) > 30:
        disp_text(screen, str(int(ball.speed * 10)),
                  (old_div(scr_width, 2) + 15, 21), main_screen_number, yellow)
    else:
        disp_text(screen, str(int(ball.speed * 10)),
                  (old_div(scr_width, 2) + 15, 21), main_screen_number, pure_red)


def check_collisions(ball, bricks, run_vars, animation_manager, sound_manager, delta_time):
    for br in bricks:
        collision_result = Collision.check(ball.get_collider(), br.collider)

        if collision_result != (0, 0):
            ball.bounce(collision_result, delta_time)
            sound_manager.play_sound(collision_sound)
            run_vars.hit_count += 1
            run_vars.brick_point += br.update(ball.speed, mute,
                                              animation_manager, sound_manager)

            animation_manager.create_new_effect(
                blast_anim2, blast_anim2_size, 3, False, (ball.x, ball.y))
            return


def render_field(pygame, screen, run_vars):
    screen.fill(black)

    # drawing prison-field
    #pygame.draw.rect(screen, grey, (100, 40, 700, 660))

    run_vars.flip_image = (run_vars.flip_image + 1) % 60
    # rendering speed images
    if run_vars.flip_image < 30:
        pygame.draw.rect(screen, black, (0, 40, 100, scr_height - 40))
    else:
        pygame.draw.rect(screen, white, (0, 40, 100, scr_height - 40))

    if run_vars.flip_image < 30:
        pygame.draw.rect(screen, white, (800, 40, 100, scr_height - 40))
    else:
        pygame.draw.rect(screen, black, (800, 40, 100, scr_height - 40))

    # drawing the prison styled thin bars
    draw_walls(screen, post_brick_width, post_brick_height)

    # drawing striker boundary
    pygame.draw.circle(screen, light_black, (main_game_middle_x,
                                             main_game_middle_y), strike_bound_radius)


def events(game_manager, pygame, screen, clock, striker, run_vars):

    events = pygame.event.get()

    for event in events:
        # quitting the game
        if event.type == pygame.QUIT:
            os._exit(0)

    # update input manager
    game_manager.input_manager.update(events)
    input = game_manager.input_manager

    # pause game
    if input.get_button('escape'):
        run_vars.pause_option = pause_game(game_manager)

    input_horizontal = input.get_axis('horizontal')
    input_vertical = input.get_axis('vertical')

    if input_horizontal == 0:
        striker.x_velocity = 0
    else:
        striker.x_velocity += input_horizontal * 0.5

    if input_vertical == 0:
        striker.y_velocity = 0
    else:
        striker.y_velocity += input_vertical * -0.5
