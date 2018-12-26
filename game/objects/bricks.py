#########################################
# Bricks Class
#########################################
from __future__ import division
import pygame
from game.global_objects import *
from past.utils import old_div
from game.misc.collisions import Rect_Collider


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

        self.collider = Rect_Collider(
            self.rect.center[0], self.rect.center[1], self.rect.width, self.rect.height)

    def draw(self, screen):
        self.image.fill(self.color)
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, white, self.rect, 2)

    def update(self, speed, mute, animation_manager, sound_manager):
        if speed <= 3:
            return 0
        self.brick_value -= old_div(speed, MAX_BALL_SPEED)
        if self.brick_value <= 0:
            # add sound for breaking
            sound_manager.play_sound(break_sound)

            # play death animation effect before dying
            animation_manager.create_new_effect(
                blast_anim1, blast_anim1_size, 3, False, (self.x, self.y))

            self.kill()
            return self.ori_brick_value * 200
        elif self.brick_value <= 3:
            self.color = brick_colors[int(math.ceil(self.brick_value)) % 3]
            return 0
        else:
            self.color = grey
            return 0
