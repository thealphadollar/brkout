##############################
# Striker Class
##############################
from __future__ import division
import pygame
from game.global_objects import *
from past.utils import old_div
from game.misc.collisions import Circle_Collider


class Striker(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_velocity = 0
        self.y_velocity = 0
        self.radius = striker_radius
        self.mass = striker_mass
        self.collider = Circle_Collider(self.x, self.y, self.radius)

    def get_collider(self):
        self.collider.x = self.x
        self.collider.y = self.y
        return self.collider

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
