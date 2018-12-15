from __future__ import absolute_import
from __future__ import division

# function to set path to current folder (py 2 to 3)
from builtins import object
from past.utils import old_div
def import_modify():
    if __name__ == '__main__':
        if __package__ is None:
            import sys
            from os import path
            sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))
try:
    from .global_funcs import *
    from .constants import *
except SystemError:
    from global_funcs import *
    from constants import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.radius = ball_radius
        self.mass = ball_mass
        self.menu_speed = menu_ball_speed
        self.speed = main_ball_speed
        self.angle = random.uniform(old_div(-math.pi,4), old_div(math.pi,4))

    def menu_screen_move(self, delta_time):
        self.x += math.sin(self.angle) * self.menu_speed * delta_time
        self.y += math.cos(self.angle) * self.menu_speed * delta_time

    def main_screen_move(self, delta_time):
        self.oldx = self.x
        self.oldy = self.y
        self.x += math.sin(self.angle) * self.speed * delta_time
        self.y += math.cos(self.angle) * self.speed * delta_time
        if self.speed > 0:
            self.speed -= (friction * delta_time)
        else:
            self.speed = 0

    # function to check collision with menu wall
    def check_collide_wall(self):
        if self.x < wall_brick_height + self.radius:
            self.x = wall_brick_height + self.radius
            self.oldx = self.x
            self.angle = -self.angle

        if self.x > scr_width - wall_brick_height - self.radius:
            self.x = scr_width - wall_brick_height - self.radius
            self.oldx = self.x
            self.angle = -self.angle

        if self.y < wall_brick_height + self.radius:
            self.y = wall_brick_height + self.radius
            self.oldy = self.y
            self.angle = math.pi - self.angle

        if self.y > scr_height - wall_brick_height - self.radius:
            self.y = scr_height - wall_brick_height - self.radius
            self.oldy = self.y
            self.angle = math.pi - self.angle

    # function to check collision with color palette
    def check_collide_palette(self):
        if (self.y < old_div(scr_height,2) + 200 + self.radius) and (self.y > old_div(scr_height,2) + 200 - self.radius):
            if (self.x < old_div(scr_width,2) + 200 + self.radius) and (self.x > old_div(scr_width,2) + 200 + self.radius - 15):
                self.x = old_div(scr_width,2) + 200 + self.radius
                self.angle = -self.angle
            elif (self.x > old_div(scr_width,2) - 200 - self.radius) and (self.x < old_div(scr_width,2) - 200 - self.radius + 15):
                self.x = old_div(scr_width,2) - 200 - self.radius
                self.angle = -self.angle

        if (self.x < old_div(scr_width,2) + 200 + self.radius) and (self.x > old_div(scr_width,2) - 200 - self.radius):
            if (self.y < old_div(scr_height,2) + 200 + self.radius) and (self.y > old_div(scr_height,2) + 200 + self.radius - 15):
                self.y = old_div(scr_height,2) + 200 + self.radius
                self.angle = math.pi - self.angle
            elif (self.y > old_div(scr_height,2) + 100 - self.radius) and (self.y < old_div(scr_height,2) + 100 - self.radius + 15):
                self.y = old_div(scr_height,2) + 100 - self.radius
                self.angle = math.pi - self.angle

    # function to check collision with losing end screen box
    def check_collide_lose(self):
        if (self.y < old_div(scr_height,2) + 230 + self.radius) and (self.y > old_div(scr_height,2) + 40 - self.radius):
            if (self.x < old_div(scr_width,2) + 250 + self.radius) and (self.x > old_div(scr_width,2) + 250 + self.radius - 15):
                self.x = old_div(scr_width,2) + 250 + self.radius
                self.angle = -self.angle
            elif (self.x > old_div(scr_width,2) - 250 - self.radius) and (self.x < old_div(scr_width,2) - 250 - self.radius + 15):
                self.x = old_div(scr_width,2) - 250 - self.radius
                self.angle = -self.angle

        if (self.x < old_div(scr_width,2) + 250 + self.radius) and (self.x > old_div(scr_width,2) - 250 - self.radius):
            if (self.y < old_div(scr_height,2) + 230 + self.radius) and (self.y > old_div(scr_height,2) + 230 + self.radius - 15):
                self.y = old_div(scr_height,2) + 230 + self.radius
                self.angle = math.pi - self.angle
            elif (self.y > old_div(scr_height,2) + 40 - self.radius) and (self.y < old_div(scr_height,2) + 40 - self.radius + 15):
                self.y = old_div(scr_height,2) + 40 - self.radius
                self.angle = math.pi - self.angle

    # function to check collision with pause screen box

    def check_collide_options(self):
        if (self.y < old_div(scr_height,2) + 208 + self.radius) and (self.y > old_div(scr_height,2) - 168 - self.radius):
            if (self.x < old_div(scr_width,2) + 178 + self.radius) and (self.x > old_div(scr_width,2) + 178 + self.radius - 15):
                self.x = old_div(scr_width,2) + 178 + self.radius
                self.angle = -self.angle
            elif (self.x > old_div(scr_width,2) - 178 - self.radius) and (self.x < old_div(scr_width,2) - 178 - self.radius + 15):
                self.x = old_div(scr_width,2) - 178 - self.radius
                self.angle = -self.angle

        if (self.x < old_div(scr_width,2) + 178 + self.radius) and (self.x > old_div(scr_width,2) - 178 - self.radius):
            if (self.y < old_div(scr_height,2) + 208 + self.radius) and (self.y > old_div(scr_height,2) + 208 + self.radius - 15):
                self.y = old_div(scr_height,2) + 208 + self.radius
                self.angle = math.pi - self.angle
            elif (self.y > old_div(scr_height,2) - 168 - self.radius) and (self.y < old_div(scr_height,2) - 168 - self.radius + 15):
                self.y = old_div(scr_height,2) - 168 - self.radius
                self.angle = math.pi - self.angle

    # checks collision with game boundary
    def check_escape(self):
        # right side
        if self.x >= scr_width - 100:
            self.angle = -self.angle
            self.x = scr_width - 100
            return 1
            # return True
        # left side
        elif self.x <= 100:
            self.angle = -self.angle
            self.x = 100
            return 1
            # return True
        # bottom
        if self.y >= scr_height:
            self.angle = math.pi - self.angle
            self.y = scr_height
            return 1
            # return True
        elif self.y <= 40:
            self.angle = math.pi - self.angle
            self.y = 40
            return 1
            # return True
        # return False

    # check collision with brick

    # horizontal brick

    # define collision with striker
    def collision_striker(self, striker):

        # distance between striker and ball
        dx = self.x - striker.x
        dy = self.y - striker.y
        distance = math.hypot(dx, dy)

        # if not colliding return
        if distance > striker.radius + self.radius:
            return False

        # using elastic collision
        approach_angle = math.atan2(dx, dy)
        ball_angle = math.atan2(math.sin(self.angle), math.cos(self.angle))
        ball_velocity_along_line = math.cos(
            approach_angle - ball_angle) * self.speed
        ball_velocity_perp_line = math.sin(
            approach_angle - ball_angle) * self.speed
        striker_velocity_along_line = (striker.x_velocity * math.sin(
            approach_angle)) + (striker.y_velocity * math.cos(approach_angle))
        striker_velocity_x_perp_line = striker.x_velocity * \
            math.cos(approach_angle)
        striker_velocity_y_perp_line = striker.y_velocity * \
            math.sin(approach_angle)
        # now this is a case of head on collision
        # setting before collision variables
        M = striker.mass
        m = self.mass
        U = striker_velocity_along_line
        u = ball_velocity_along_line
        # velocities after elastic collision
        striker_velocity_along_line = old_div((((M-m) * U) + (2 * m * u)), (M + m))
        ball_velocity_along_line = U - u + striker_velocity_along_line
        # setting values after collision
        striker.x_velocity = math.hypot(
            striker_velocity_along_line, striker_velocity_x_perp_line)
        striker.y_velocity = math.hypot(
            striker_velocity_along_line, striker_velocity_y_perp_line)
        self.speed = math.hypot(ball_velocity_along_line,
                                ball_velocity_perp_line)
        ball_x_velocity = ball_velocity_along_line * \
            math.sin(approach_angle) - ball_velocity_perp_line * \
            math.cos(approach_angle)
        ball_y_velocity = ball_velocity_along_line * \
            math.cos(approach_angle) + ball_velocity_perp_line * \
            math.sin(approach_angle)
        self.angle = math.atan2(ball_x_velocity, ball_y_velocity)

        if self.speed > MAX_BALL_SPEED:
            self.speed = MAX_BALL_SPEED
        if abs(striker.x_velocity) > MAX_STRIKER_SPEED:
            striker.x_velocity = MAX_STRIKER_SPEED * \
                (old_div(striker.x_velocity, abs(striker.x_velocity)))
        if abs(striker.y_velocity) > MAX_STRIKER_SPEED:
            striker.y_velocity = MAX_STRIKER_SPEED * \
                (old_div(striker.y_velocity, abs(striker.y_velocity)))

        angle = math.atan2(dx, dy)
        self.x = striker.x + ((striker.radius + self.radius) * math.sin(angle))
        self.y = striker.y + ((striker.radius + self.radius) * math.cos(angle))
        self.oldx = self.x
        self.oldy = self.y

        return True

    def draw(self, screen):
        pygame.draw.circle(
            screen, yellow, (int(self.x), int(self.y)), self.radius)


# striker class
class Striker(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_velocity = 0
        self.y_velocity = 0
        self.radius = striker_radius
        self.mass = striker_mass

    def update(self, delta_time):
        self.x += self.x_velocity * delta_time
        self.y += self.y_velocity * delta_time
        if self.x_velocity > 0:
            self.x_velocity -= striker_friction * delta_time
            if self.x_velocity < 0:
                self.x_velocity = 0
        elif self.x_velocity < 0:
            self.x_velocity += striker_friction * delta_time
            if self.x_velocity > 0:
                self.x_velocity = 0
        if self.y_velocity > 0:
            self.y_velocity -= striker_friction * delta_time
            if self.y_velocity < 0:
                self.y_velocity = 0
        elif self.y_velocity < 0:
            self.y_velocity += striker_friction * delta_time
            if self.y_velocity > 0:
                self.y_velocity = 0

        if abs(self.y_velocity) > MAX_STRIKER_SPEED:
            self.y_velocity = MAX_STRIKER_SPEED * \
                (old_div(self.y_velocity, abs(self.y_velocity)))
        if abs(self.x_velocity) > MAX_STRIKER_SPEED:
            self.x_velocity = MAX_STRIKER_SPEED * \
                (old_div(self.x_velocity, abs(self.x_velocity)))

    def check_bound(self):
        dx = self.x - main_game_middle_x
        dy = self.y - main_game_middle_y
        distance = math.hypot(dx, dy)
        if distance < strike_bound_radius - self.radius:
            return

        self.x_velocity = 0
        self.y_velocity = 0

        angle = math.atan2(dx, dy)
        self.x = main_game_middle_x + \
            ((strike_bound_radius - self.radius) * math.sin(angle))
        self.y = main_game_middle_y + \
            ((strike_bound_radius - self.radius) * math.cos(angle))

    def draw(self, screen, color):
        pygame.draw.circle(
            screen, color, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(screen, silver, (int(self.x),
                                            int(self.y)), self.radius, 1)
        pygame.draw.circle(screen, wall_silver, (int(
            self.x), int(self.y)), self.radius - 10, 1)
        pygame.draw.circle(screen, wall_silver, (int(
            self.x), int(self.y)), self.radius - 30, 1)


class Bricks(pygame.sprite.Sprite):
    def __init__(self, x, y, VH):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.brick_value = random.randint(1, 3)
        self.ori_brick_value = self.brick_value
        self.type = VH
        self.color = brick_colors[self.brick_value % 3]
        if random.random() > 0.94:
            self.brick_value = 1000000007
            # self.color = grey
        if VH == 1:
            self.image = pygame.Surface(
                (horizontal_brick_width, horizontal_brick_height))
            self.image.fill(self.color)
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
        elif VH == 0:
            self.image = pygame.Surface(
                (vertical_brick_width, vertical_brick_height))
            self.image.fill(self.color)
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
        self.health = self.brick_value * 100

    def draw23(self, screen):
        self.image.fill(self.color)
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, white, self.rect, 2)

    def check_hor_coll(self, ball):
        # lower side
        # returns true if collision takes place
        did_collide = False
        x, y = self.x, self.y
        # lower side
        if (ball.x > x - ball.radius) and (ball.x < x + horizontal_brick_width + ball.radius):
            if (ball.y < y + horizontal_brick_height + ball.radius) and (ball.y > y + horizontal_brick_height):
                ball.y = y + horizontal_brick_height + ball.radius
                ball.angle = math.pi - ball.angle
                did_collide = True
        # upper side

            elif (ball.y > y - ball.radius) and (ball.y < y):
                ball.y = y - ball.radius
                ball.angle = math.pi - ball.angle
                did_collide = True
        # left side
        if (ball.y < y + horizontal_brick_height + ball.radius) and (ball.y > y - ball.radius):
            if (ball.x > x - ball.radius) and (ball.x < x):
                ball.x = x - ball.radius
                ball. angle = -ball.angle
                did_collide = True
        # right side

            elif (ball.x < x + horizontal_brick_width + ball.radius) and (ball.x > x + horizontal_brick_width):
                ball.x = x + horizontal_brick_width + ball.radius
                ball.angle = -ball.angle
                did_collide = True
        return did_collide

    def check_ver_coll(self, ball):
        # lower side
        # returns true is collision takes place
        did_collide = False
        x, y = self.x, self.y
        if (ball.x > x - ball.radius) and (ball.x < x + vertical_brick_width + ball.radius):
            if (ball.y < y + vertical_brick_height + ball.radius) and (ball.y > y + vertical_brick_height):
                ball.y = y + vertical_brick_height + ball.radius
                ball.angle = math.pi - ball.angle
                did_collide = True
            # upper side
            elif (ball.y > y - ball.radius) and (ball.y < y):
                ball.y = y - ball.radius
                ball.angle = math.pi - ball.angle
                did_collide = True
        # left side
        if (ball.y < y + vertical_brick_height + ball.radius) and (ball.y > y - ball.radius):
            if (ball.x > x - ball.radius) and (ball.x < x):
                ball.x = x - ball.radius
                ball. angle = -ball.angle
                did_collide = True
            # right side
            elif (ball.x < x + vertical_brick_width + ball.radius) and (ball.x > x + vertical_brick_width):
                ball.x = x + vertical_brick_width + ball.radius
                ball.angle = -ball.angle
                did_collide = True
        return did_collide

    def update(self, speed, mute, animation_manager):
        if speed <= 3:
            return 0
        self.brick_value -= old_div(speed, MAX_BALL_SPEED)
        if self.brick_value <= 0:
            # add sound for breaking
            if mute==1:
            	break_sound.set_volume(2)
            	break_sound.play()

            # play death animation effect before dying
            animation_manager.create_new_effect(blast_anim1, blast_anim1_size, 2, False, (self.x, self.y))

            self.kill()
            return self.ori_brick_value * 200
        elif self.brick_value <= 3:
            self.color = brick_colors[int(math.ceil(self.brick_value)) % 3]
            return 0
        else:
            self.color = grey
            return 0
