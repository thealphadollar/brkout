#########################################
# Bricks Class
#########################################
from __future__ import division
import pygame
from game.global_objects import *
from past.utils import old_div


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
            if mute == 1:
                break_sound.set_volume(2)
                break_sound.play()

            # play death animation effect before dying
            animation_manager.create_new_effect(
                blast_anim1, blast_anim1_size, 2, False, (self.x, self.y))

            self.kill()
            return self.ori_brick_value * 200
        elif self.brick_value <= 3:
            self.color = brick_colors[int(math.ceil(self.brick_value)) % 3]
            return 0
        else:
            self.color = grey
            return 0
