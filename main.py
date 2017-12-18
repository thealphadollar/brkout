from start_screen import menu_screen
from credits_screen import credits_screen
from global_funcs import *
from global_objects import *
from constants import *
import os

# function to initialise pygame


def init():

    global screen, clock, flip_image, score, seconds_first, seconds_second, minutes_first, minutes_second, count_to_seconds, ball, striker
    ball = Ball(main_game_middle_x, main_game_middle_y + strike_bound_radius)
    striker = Striker(main_game_middle_x, main_game_middle_y)
    seconds_first, seconds_second = 0, 0
    minutes_first, minutes_second = 0, 0
    count_to_seconds = 0
    score = 0
    flip_image = 0

    # initialising sound system
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.init()

    # initialising display
    gamelogo = pygame.image.load(os.path.join(assets_directory, 'logo.png'))
    pygame.display.set_icon(gamelogo)
    pygame.display.set_caption("BrkOut")
    screen = pygame.display.set_mode((scr_width, scr_height))

    # initialising time
    clock = pygame.time.Clock()


# function to show time


def show_time(start_timer):
    global count_to_seconds, seconds_second, seconds_first, minutes_first, minutes_second

    if start_timer:
        count_to_seconds += 1

    if count_to_seconds == 60:
        seconds_first += 1
        count_to_seconds = 0
    if seconds_first == 10:
        seconds_second += 1
        seconds_first = 0
    if seconds_second == 6:
        minutes_first += 1
        seconds_second = 0
    if minutes_first == 10:
        minutes_second += 1
        minutes_first = 0

    # displaying time label
    disp_text(screen, "runtime : ", (scr_width - 110, 21), main_screen_text, silver)
    disp_text(screen, str(minutes_second)+str(minutes_first)+":"+str(seconds_second)+str(seconds_first),
              (scr_width - 40, 21), main_screen_number, silver)


# function to show score()


def show_score():
    global score

    # score logic to be implemented

    # method same as show_time to be adopted for displaying

    # displaying score label
    disp_text(screen, "score : ", (50, 21), main_screen_text, silver)
    disp_text(screen, "1024", (100, 21), main_screen_number, silver)


# function to show ball speed
def show_speed(ball):

    disp_text(screen, "speed :", (scr_width/2 - 30, 21), main_screen_text, silver)
    if (ball.speed * 5) > 60:
        disp_text(screen, str(int(ball.speed * 5)), (scr_width/2 + 15, 21), main_screen_number, pure_green)
    elif (ball.speed * 5) > 20:
        disp_text(screen, str(int(ball.speed * 5)), (scr_width / 2 + 15, 21), main_screen_number, yellow)
    else:
        disp_text(screen, str(int(ball.speed * 5)), (scr_width / 2 + 15, 21), main_screen_number, pure_red)


# rendering static elements


def render_field():

    global flip_image

    screen.fill(black)

    # drawing prison-field
    pygame.draw.rect(screen, grey, (100, 40, 700, 660))

    flip_image = (flip_image + 1) % 20
    # rendering speed images
    if flip_image < 10:
        screen.blit(speed_red, (0, 40))
    else:
        screen.blit(speed_blue, (0, 40))

    if flip_image < 10:
        screen.blit(speed_red, (800, 40))
    else:
        screen.blit(speed_blue, (800, 40))

    # drawing the prison styled thin bars
    draw_walls(screen, post_brick_width, post_brick_height)

    # drawing striker boundary
    pygame.draw.circle(screen, light_black, (main_game_middle_x, main_game_middle_y), strike_bound_radius)

# main game loop


def gameloop(striker_color):
    global screen, clock, ball, striker
    start_time = False

    while True:

        # time passed
        delta_time = clock.get_time() / 10

        render_field()

        # getting in events
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                # pausing the game
                if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                    #pause_game() function to add pause game
                    pass

            # stopping striker once key is lifted
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    striker.y_velocity = 0
                if event.key == pygame.K_UP:
                    striker.y_velocity = 0
                if event.key == pygame.K_RIGHT:
                    striker.x_velocity = 0
                if event.key == pygame.K_LEFT:
                    striker.x_velocity = 0

            # quitting the game
            if event.type == pygame.QUIT:
                os._exit(0)

        # updating striker
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            striker.x_velocity += .5
        if pressed[pygame.K_LEFT]:
            striker.x_velocity -= .5
        if pressed[pygame.K_UP]:
            striker.y_velocity -= .5
        if pressed[pygame.K_DOWN]:
            striker.y_velocity += .5


        # updating elements
        striker.update(delta_time)
        ball.main_screen_move(delta_time)
        striker.check_bound()

        # check first strike to start timer
        if not start_time:
            start_time = ball.collision_striker(striker)
        else:
            ball.collision_striker(striker)

        ball.check_escape()

        # rendering various elements
        striker.draw(screen, striker_color)
        ball.draw(screen)

        # show time function
        show_time(start_time)
        # show score
        show_score()
        # show speed
        show_speed(ball)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":

    while True:
        init()  # used to initialise the pygame module
        choice, color_choice = menu_screen(screen, clock)

        if choice == 0:
            gameloop(striker_colors[color_choice])
        elif choice == 1:
            credits_screen(screen, clock)
