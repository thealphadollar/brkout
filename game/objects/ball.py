##############################
# Ball class
##############################
import pygame
from game.constants import *
from game.global_funcs import *
from past.utils import old_div


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.radius = ball_radius
        self.mass = ball_mass
        self.menu_speed = menu_ball_speed
        self.speed = main_ball_speed
        self.angle = random.uniform(old_div(-math.pi, 4), old_div(math.pi, 4))

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
        if (self.y < old_div(scr_height, 2) + 200 + self.radius) and (self.y > old_div(scr_height, 2) + 200 - self.radius):
            if (self.x < old_div(scr_width, 2) + 200 + self.radius) and (self.x > old_div(scr_width, 2) + 200 + self.radius - 15):
                self.x = old_div(scr_width, 2) + 200 + self.radius
                self.angle = -self.angle
            elif (self.x > old_div(scr_width, 2) - 200 - self.radius) and (self.x < old_div(scr_width, 2) - 200 - self.radius + 15):
                self.x = old_div(scr_width, 2) - 200 - self.radius
                self.angle = -self.angle

        if (self.x < old_div(scr_width, 2) + 200 + self.radius) and (self.x > old_div(scr_width, 2) - 200 - self.radius):
            if (self.y < old_div(scr_height, 2) + 200 + self.radius) and (self.y > old_div(scr_height, 2) + 200 + self.radius - 15):
                self.y = old_div(scr_height, 2) + 200 + self.radius
                self.angle = math.pi - self.angle
            elif (self.y > old_div(scr_height, 2) + 100 - self.radius) and (self.y < old_div(scr_height, 2) + 100 - self.radius + 15):
                self.y = old_div(scr_height, 2) + 100 - self.radius
                self.angle = math.pi - self.angle

    # function to check collision with losing end screen box
    def check_collide_lose(self):
        if (self.y < old_div(scr_height, 2) + 230 + self.radius) and (self.y > old_div(scr_height, 2) + 40 - self.radius):
            if (self.x < old_div(scr_width, 2) + 250 + self.radius) and (self.x > old_div(scr_width, 2) + 250 + self.radius - 15):
                self.x = old_div(scr_width, 2) + 250 + self.radius
                self.angle = -self.angle
            elif (self.x > old_div(scr_width, 2) - 250 - self.radius) and (self.x < old_div(scr_width, 2) - 250 - self.radius + 15):
                self.x = old_div(scr_width, 2) - 250 - self.radius
                self.angle = -self.angle

        if (self.x < old_div(scr_width, 2) + 250 + self.radius) and (self.x > old_div(scr_width, 2) - 250 - self.radius):
            if (self.y < old_div(scr_height, 2) + 230 + self.radius) and (self.y > old_div(scr_height, 2) + 230 + self.radius - 15):
                self.y = old_div(scr_height, 2) + 230 + self.radius
                self.angle = math.pi - self.angle
            elif (self.y > old_div(scr_height, 2) + 40 - self.radius) and (self.y < old_div(scr_height, 2) + 40 - self.radius + 15):
                self.y = old_div(scr_height, 2) + 40 - self.radius
                self.angle = math.pi - self.angle

    # function to check collision with pause screen box

    def check_collide_options(self):
        if (self.y < old_div(scr_height, 2) + 208 + self.radius) and (self.y > old_div(scr_height, 2) - 168 - self.radius):
            if (self.x < old_div(scr_width, 2) + 178 + self.radius) and (self.x > old_div(scr_width, 2) + 178 + self.radius - 15):
                self.x = old_div(scr_width, 2) + 178 + self.radius
                self.angle = -self.angle
            elif (self.x > old_div(scr_width, 2) - 178 - self.radius) and (self.x < old_div(scr_width, 2) - 178 - self.radius + 15):
                self.x = old_div(scr_width, 2) - 178 - self.radius
                self.angle = -self.angle

        if (self.x < old_div(scr_width, 2) + 178 + self.radius) and (self.x > old_div(scr_width, 2) - 178 - self.radius):
            if (self.y < old_div(scr_height, 2) + 208 + self.radius) and (self.y > old_div(scr_height, 2) + 208 + self.radius - 15):
                self.y = old_div(scr_height, 2) + 208 + self.radius
                self.angle = math.pi - self.angle
            elif (self.y > old_div(scr_height, 2) - 168 - self.radius) and (self.y < old_div(scr_height, 2) - 168 - self.radius + 15):
                self.y = old_div(scr_height, 2) - 168 - self.radius
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
        striker_velocity_along_line = old_div(
            (((M - m) * U) + (2 * m * u)), (M + m))
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
