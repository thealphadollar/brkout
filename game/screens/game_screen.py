from __future__ import absolute_import
from __future__ import division
from game.objects import *
from game.global_objects import *
from game.gui_package import *
from game.misc import *
from game.screens.pause_screen import *
from past.utils import old_div

# function to set path to current folder (py 2 to 3)


def import_modify():
    if __name__ == '__main__':
        if __package__ is None:
            import sys
            from os import path
            sys.path.append(path.abspath(
                path.join(path.dirname(__file__), '..')))


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

    bricks = pygame.sprite.Group()
    add_to_group(bricks)

    start_timer = False

    pygame.joystick.init()

    # Joystick initialized
    joystick = None

    joystick_count = pygame.joystick.get_count()
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

    while True:

        # time passed
        delta_time = old_div(clock.get_time(), 10)

        # drawing the game field
        render_field(pygame, screen, run_vars)

        # getting the events
        events(game_manager, pygame, screen,
               clock, joystick, striker, run_vars)

        # returning pause options if it is not resume
        if run_vars.pause_option is not E_Pause_Option.resume:
            return run_vars.pause_option, run_vars

        # updating elements
        striker.update(delta_time)
        ball.main_screen_move(delta_time)
        striker.check_bound()

        # checking collisions
        check_collisions(ball, bricks, run_vars,
                         animation_manager, sound_manager)

        # check first strike to start timer
        if not start_timer:
            start_timer = ball.collision_striker(striker)

            # correct code for striker sound
#            if start_time:
#                striker_sound.set_volume(1)
#                striker_sound.play()

        else:
            if ball.collision_striker(striker):
                pass

                # correct code for striker sound
#                striker_sound.set_volume(1)
#                striker_sound.play()

        # checking winning
        if ball.check_escape():
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
            br.draw23(screen)

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


def check_collisions(ball, bricks, run_vars, animation_manager, sound_manager):
    for br in bricks:
        if br.type == 1:
            did_collide = br.check_hor_coll(ball)
        else:
            did_collide = br.check_ver_coll(ball)

        # returns if collision has taken place
        if did_collide:
            sound_manager.play_sound(collision_sound)
            run_vars.hit_count += 1
            run_vars.brick_point += br.update(ball.speed, mute,
                                              animation_manager, sound_manager)

            # play ball hit animati0n effect
            animation_manager.create_new_effect(
                blast_anim2, blast_anim2_size, 0, False, (ball.x, ball.y))


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


def events(game_manager, pygame, screen, clock, joystick, striker, run_vars):
    # Jostick variable initizlization
    hat = False
    axis1 = False
    axis2 = False
    axis3 = False
    axis4 = False

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            # pausing the game
            if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                # pause_game() function
                run_vars.pause_option = pause_game(game_manager)

        # quitting the game
        if event.type == pygame.QUIT:
            os._exit(0)

    # updating striker
    if joystick != None:
        if joystick.get_numaxes() >= 4:
            hat = joystick.get_hat(0)
            axis1 = joystick.get_axis(0)
            axis2 = joystick.get_axis(1)
            axis3 = joystick.get_axis(2)
            axis4 = joystick.get_axis(3)
        else:
            hat = False
            axis1 = False
            axis2 = False
            axis3 = False
            axis4 = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] or pressed[pygame.K_d] or hat == (1, 0) or axis1 >= 0.7 or axis3 >= 0.7:
        striker.x_velocity += .5
    elif pressed[pygame.K_LEFT] or pressed[pygame.K_a] or hat == (-1, 0) or axis1 <= -0.7 or axis3 <= -0.7:
        striker.x_velocity -= .5
    else:
        striker.x_velocity = 0
    if pressed[pygame.K_UP] or pressed[pygame.K_w] or hat == (0, 1) or axis2 <= -0.7 or axis4 <= -0.7:
        striker.y_velocity -= .5
    elif pressed[pygame.K_DOWN] or pressed[pygame.K_s] or hat == (0, -1) or axis2 >= 0.7 or axis4 >= 0.7:
        striker.y_velocity += .5
    else:
        striker.y_velocity = 0
