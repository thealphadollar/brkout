from constants import *
import random
import math


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = ball_radius
        self.mass = ball_mass
        self.speed = menu_ball_speed
        self.angle = random.uniform(-math.pi/2, math.pi/2)

    def move(self, delta_time):
        self.x += math.sin(self.angle) * self.speed * delta_time
        self.y += math.cos(self.angle) * self.speed * delta_time

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
        #pygame.draw.rect(screen, white, (scr_width/2 - 200, scr_height/2 + 40, 400, 100), 2)
        if (self.y < scr_height/2 + 140 + self.radius) and (self.y > scr_height/2 + 40 - self.radius):
            if (self.x < scr_width/2 + 200 + self.radius) and (self.x > scr_width/2 + 200 + self.radius - 20):
                self.x = scr_width/2 + 200 + self.radius
                self.angle = -self.angle
            elif (self.x > scr_width/2 - 200 - self.radius) and (self.x < scr_width/2 - 200 - self.radius + 20):
                self.x = scr_width/2 - 200 - self.radius
                self.angle = -self.angle

        if (self.x < scr_width/2 + 200 + self.radius) and (self.x > scr_width/2 - 200 - self.radius):
            if (self.y < scr_height/2 + 140 + self.radius) and (self.y > scr_height/2 + 140 + self.radius - 20):
                self.y = scr_height/2 + 140 + self.radius
                self.angle = math.pi - self.angle
            elif (self.y > scr_height/2 + 40 - self.radius) and (self.y < scr_height/2 + 40 - self.radius + 20):
                self.y = scr_height/2 + 40 - self.radius
                self.angle = math.pi - self.angle

    def draw(self, screen):
        pygame.draw.circle(screen, yellow, (int(self.x), int(self.y)), self.radius)


