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
        # either 400, 500 or 600
        self.health = random.randint(4, 6) * 100
        if self.health == 600:
            self.health = 599
        self.ori_health = self.health
        self.type = VH
        if random.random() > 0.94:
            self.health = 100000000

        if VH == 1:
            self.image = brick_imgs_h[self.get_health_index()]
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
        elif VH == 0:
            self.image = brick_imgs_v[self.get_health_index()]
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)

        self.collider = Rect_Collider(
            self.rect.center[0], self.rect.center[1], self.rect.width, self.rect.height)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, speed, mute, animation_manager, sound_manager, run_vars):
        if speed <= 3:
            return 0

        self.health -= old_div(speed, MAX_BALL_SPEED) * 180 * run_vars.damage_multiplier

        if self.type == 1:
            self.image = brick_imgs_h[self.get_health_index()]
        else:
            self.image = brick_imgs_v[self.get_health_index()]

        if self.health <= 0:
            # add sound for breaking
            sound_manager.play_sound(break_sound)

            # play death animation effect before dying
            animation_manager.create_new_effect(
                blast_anim1, blast_anim1_size, 3, False, (self.x, self.y))

            self.kill()
            return self.ori_health * 0.5
        else:
            return 0

    def get_health_index(self):
        health_index = self.health // 100
        if health_index > 6:
            health_index = 6
        return int(health_index)
