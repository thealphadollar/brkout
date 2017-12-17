from constants import *
import random
import math


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = ball_radius
        self.mass = ball_mass
        self.menu_speed = menu_ball_speed
        self.speed = main_ball_speed
        self.angle = random.uniform(-math.pi/2, math.pi/2)

    def menu_screen_move(self, delta_time):
        self.x += math.sin(self.angle) * self.menu_speed * delta_time
        self.y += math.cos(self.angle) * self.menu_speed * delta_time

    def main_screen_move(self, delta_time):
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
            self.angle = -self.angle

        if self.x > scr_width - wall_brick_height - self.radius:
            self.x = scr_width - wall_brick_height - self.radius
            self.angle = -self.angle

        if self.y < wall_brick_height + self.radius:
            self.y = wall_brick_height + self.radius
            self.angle = math.pi - self.angle

        if self.y > scr_height - wall_brick_height - self.radius:
            self.y = scr_height - wall_brick_height - self.radius
            self.angle = math.pi - self.angle

    # function to check collision with color palette
    def check_collide_palette(self):
        if (self.y < scr_height/2 + 140 + self.radius) and (self.y > scr_height/2 + 40 - self.radius):
            if (self.x < scr_width/2 + 200 + self.radius) and (self.x > scr_width/2 + 200 + self.radius - 15):
                self.x = scr_width/2 + 200 + self.radius
                self.angle = -self.angle
            elif (self.x > scr_width/2 - 200 - self.radius) and (self.x < scr_width/2 - 200 - self.radius + 15):
                self.x = scr_width/2 - 200 - self.radius
                self.angle = -self.angle

        if (self.x < scr_width/2 + 200 + self.radius) and (self.x > scr_width/2 - 200 - self.radius):
            if (self.y < scr_height/2 + 140 + self.radius) and (self.y > scr_height/2 + 140 + self.radius - 15):
                self.y = scr_height/2 + 140 + self.radius
                self.angle = math.pi - self.angle
            elif (self.y > scr_height/2 + 40 - self.radius) and (self.y < scr_height/2 + 40 - self.radius + 15):
                self.y = scr_height/2 + 40 - self.radius
                self.angle = math.pi - self.angle

    # check collision with brick

    # horizontal brick
    def collision_horizontal_brick(self, horizontal_brick):
        # lower side
        x, y = horizontal_brick.get_pos()
        if (self.x > x - self.radius) and (self.x < x + horizontal_brick_width + self.radius):
            if (self.y < y + horizontal_brick_height + self.radius) and (self.y > y + horizontal_brick_height):
                self.y = y + horizontal_brick_height + self.radius
                self.angle = math.pi - self.angle
        # upper side
        elif (self.x > x - self.radius) and (self.x < x + horizontal_brick_width + self.radius):
            if (self.y > y - self.radius) and (self.y < y):
                self.y = y - self.radius
                self.angle = math.pi - self.angle
        # left side
        if (self.y < y + horizontal_brick_height + self.radius) and (self.y > y - self.radius):
            if (self.x > x - self.radius) and (self.x < x):
                self.x = x - self.radius
                self. angle = -self.angle
        # right side
        elif (self.y < y + horizontal_brick_height + self.radius) and (self.y > y - self.radius):
            if (self.x < x + horizontal_brick_width + self.radius) and (self.x > x + horizontal_brick_width):
                self.x = x + horizontal_brick_width + self.radius
                self.angle = -self.angle

    # vertical brick
    def collision_vertical_brick(self, vertical_brick):
        # lower side
        x, y = vertical_brick.get_pos()
        if (self.x > x - self.radius) and (self.x < x + vertical_brick_width + self.radius):
            if (self.y < y + vertical_brick_height + self.radius) and (self.y > y + vertical_brick_height):
                self.y = y + vertical_brick_height + self.radius
                self.angle = math.pi - self.angle
        # upper side
        elif (self.x > x - self.radius) and (self.x < x + vertical_brick_width + self.radius):
            if (self.y > y - self.radius) and (self.y < y):
                self.y = y - self.radius
                self.angle = math.pi - self.angle
        # left side
        if (self.y < y + vertical_brick_height + self.radius) and (self.y > y - self.radius):
            if (self.x > x - self.radius) and (self.x < x):
                self.x = x - self.radius
                self. angle = -self.angle
        # right side
        elif (self.y < y + vertical_brick_height + self.radius) and (self.y > y - self.radius):
            if (self.x < x + vertical_brick_width + self.radius) and (self.x > x + vertical_brick_width):
                self.x = x + vertical_brick_width + self.radius
                self.angle = -self.angle

    # define collision with striker


    def draw(self, screen):
        pygame.draw.circle(screen, yellow, (int(self.x), int(self.y)), self.radius)


