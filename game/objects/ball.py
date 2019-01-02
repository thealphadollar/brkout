##############################
# Ball class
##############################
import pygame
from game.global_objects import *
from past.utils import old_div
from game.misc.collisions import *
import math
import random


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
        self.collider = Circle_Collider(self.x, self.y, self.radius)
        self.angular_speed = 0
        self.ball_img_unrotated = ball_img.convert_alpha()
        self.ball_img_rotated = ball_img.convert_alpha()
        self.total_rotation = 0

    def get_collider(self):
        self.collider.x = self.x
        self.collider.y = self.y
        return self.collider

    def bounce(self, normal, delta_time):
        speed_x = math.sin(self.angle)
        speed_y = math.cos(self.angle)

        self.x += normal[0] * self.menu_speed * delta_time
        self.y += normal[1] * self.menu_speed * delta_time

        if normal == (0, -1) or normal == (0, 1):       # normal up or down
            speed_y = -speed_y
        else:                                           # normal right of left
            speed_x = -speed_x

        self.angle = math.atan2(speed_x, speed_y)
        if random.random() < 0.5:
            self.angular_speed = max_angular_speed
        else:
            self.angular_speed = -max_angular_speed

    def menu_screen_move(self, delta_time):
        self.x += math.sin(self.angle) * self.menu_speed * delta_time
        self.y += math.cos(self.angle) * self.menu_speed * delta_time

        if self.angular_speed == 0:
            self.angular_speed = 0
        elif self.angular_speed > 0:
            self.angular_speed -= (angular_friction * delta_time)
        else:
            self.angular_speed += (angular_friction * delta_time)

        self.total_rotation += self.angular_speed * delta_time
        self.rotate_ball(delta_time)

    def rotate_ball(self, delta_time):
        self.ball_img_rotated = pygame.transform.rotate(
            self.ball_img_unrotated, self.total_rotation)

    def main_screen_move(self, delta_time, current_friction):
        self.oldx = self.x
        self.oldy = self.y
        self.x += math.sin(self.angle) * self.speed * delta_time
        self.y += math.cos(self.angle) * self.speed * delta_time
        if self.speed > 0:
            self.speed -= (current_friction * delta_time)
        else:
            self.speed = 0

        if self.angular_speed == 0:
            self.angular_speed = 0
        elif self.angular_speed > 0:
            self.angular_speed -= (angular_friction * delta_time)
        else:
            self.angular_speed += (angular_friction * delta_time)

        self.total_rotation += self.angular_speed * delta_time
        self.rotate_ball(delta_time)

    # checks collision with game boundary
    def check_escape(self, game_area_collider):
        coll = Collision.check(self.get_collider(), game_area_collider)
        if coll != (0, 0):      # ball in game area
            return False
        else:                   # ball outside game area
            return True

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
        img_rect = self.ball_img_rotated.get_rect(center=(self.x, self.y))
        screen.blit(self.ball_img_rotated, img_rect.topleft)
