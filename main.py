from start_screen import menu_screen
from credits_screen import credits_screen
from global_funcs import *
from global_objects import *
from constants import *
import os

# function to initialise pygame


def init():

    global screen, clock, flip_image, score, seconds_first, seconds_second, minutes_first, minutes_second, \
        count_to_seconds, ball, striker, time_count, score_time, hit_count, brick_point

    hit_count = 0  # stores number of bricks hit
    brick_point = 0  # stores the score accumulated by hitting brick
    score_time = 0  # timer for the score calculation
    time_count = 0  # increases score_time after 60 frames
    ball = Ball(main_game_middle_x + 50, main_game_middle_y + strike_bound_radius - 75)
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

def add_to_group():
    y=0
    while y<4:
        x=100 + y*vertical_brick_width
        while x < 800-y*vertical_brick_width:
            b = Bricks(x,40 + y*horizontal_brick_height,1)
            bricks.add(b)
            x += horizontal_brick_width
        y += 1
    y=0   
    while y<4:
        x=100 + y*vertical_brick_width
        while x < 800-y*vertical_brick_width:
            b = Bricks(x,670 - y*horizontal_brick_height,1)
            bricks.add(b)
            x += horizontal_brick_width
        y += 1
    x=1
    while x<5:
        y= 40 + x*horizontal_brick_height 
        while y < 700 - x*horizontal_brick_height:
            b= Bricks( 100 + (x-1)*vertical_brick_width, y, 0)
            bricks.add(b)
            y += vertical_brick_height
        x+=1
    
    x=1
    while x<5:
        y= 40 + x*horizontal_brick_height 
        while y < 700 - x*horizontal_brick_height:
            b= Bricks( 800 - x*vertical_brick_width, y, 0)
            bricks.add(b)
            y += vertical_brick_height
        x+=1


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


def show_score(start_timer):
    global score, time_count, score_time, hit_count, brick_point
    # keeping track of time for scoring
    if start_timer:
        time_count += 1

    # updating score variable
    if time_count == 60:
        score_time += 1
        time_count = 0
    
    if score_time > 0:
        score = int(brick_point / (.7 * math.sqrt(score_time) + .3 * (hit_count ** (1.0/3))))

    # negative score not allowed
    if score < 0:
        score = 0

    # method same as show_time to be adopted for displaying

    # displaying score label
    disp_text(screen, "score : ", (50, 21), main_screen_text, silver)
    disp_text(screen, str(score), (100, 21), main_screen_number, silver)



# function to show ball speed
def show_speed(ball):

    disp_text(screen, "speed :", (scr_width/2 - 30, 21), main_screen_text, silver)
    if (ball.speed * 10) > 80:
        disp_text(screen, str(int(ball.speed * 10)), (scr_width/2 + 15, 21), main_screen_number, pure_green)
    elif (ball.speed * 10) > 20:
        disp_text(screen, str(int(ball.speed * 10)), (scr_width / 2 + 15, 21), main_screen_number, yellow)
    else:
        disp_text(screen, str(int(ball.speed * 10)), (scr_width / 2 + 15, 21), main_screen_number, pure_red)


# rendering static elements

def check_collisions():
    global hit_count, brick_point
    for br in bricks:
        if br.type == 1:
            did_collide = br.check_hor_coll(ball)
        else:
            did_collide = br.check_ver_coll(ball)
        if did_collide:
            hit_count += 1
            brick_point += br.update(ball.speed)

def render_field():

    global flip_image

    screen.fill(black)

    # drawing prison-field
    #pygame.draw.rect(screen, grey, (100, 40, 700, 660))

    flip_image = (flip_image + 1) % 40
    # rendering speed images
    if flip_image < 20:
        screen.blit(speed_red, (-2, 40))
    else:
        screen.blit(speed_blue, (-2, 40))

    if flip_image < 20:
        screen.blit(speed_red, (802, 40))
    else:
        screen.blit(speed_blue, (802, 40))

    # drawing the prison styled thin bars
    draw_walls(screen, post_brick_width, post_brick_height)

    # drawing striker boundary
    pygame.draw.circle(screen, light_black, (main_game_middle_x, main_game_middle_y), strike_bound_radius)

# main game loop

def events():
    # getting in events
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            # pausing the game
            if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                #pause_game() function to add pause game
                pass           
        # quitting the game
        if event.type == pygame.QUIT:
            os._exit(0)

    # updating striker
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        striker.x_velocity += .5
    elif pressed[pygame.K_LEFT]:
        striker.x_velocity -= .5
    else:
        striker.x_velocity = 0
    if pressed[pygame.K_UP]:
        striker.y_velocity -= .5
    elif pressed[pygame.K_DOWN]:
        striker.y_velocity += .5
    else:
        striker.y_velocity = 0

def gameloop(striker_color):
    global screen, clock, ball, striker
    start_time = False

    while True:

        # time passed
        delta_time = clock.get_time() / 10
       
       #drawing the game field
        render_field()

        # getting the events
        events()

        # updating elements
        striker.update(delta_time)
        ball.main_screen_move(delta_time)
        striker.check_bound()

        # checking collisions
        check_collisions()

        # check first strike to start timer
        if not start_time:
            start_time = ball.collision_striker(striker)
        else:
            ball.collision_striker(striker)

        if ball.check_escape():
            temp_time = pygame.time.get_ticks()
            while pygame.time.get_ticks() - temp_time < 400:
                pass
            return 1

        # rendering various elements
        striker.draw(screen, striker_color)
        ball.draw(screen)
        # show bricks
        for br in bricks:
            br.draw23(screen)

        # show time function
        show_time(start_time)
        # show score
        show_score(start_time)
        # show speed
        show_speed(ball)
        if ball.speed == 0 and start_time:
            temp_time = pygame.time.get_ticks()
            while pygame.time.get_ticks() - temp_time < 400:
                pass
            return 0
        pygame.display.update()
        clock.tick(FPS)

bricks = pygame.sprite.Group()
add_to_group()

if __name__ == "__main__":

    while True:
        init()  # used to initialise the pygame module
        choice, color_choice = menu_screen(screen, clock)
        if choice == 0:
            end_choice = gameloop(striker_colors[color_choice])
            os._exit(0)
        elif choice == 1:
            credits_screen(screen, clock)
