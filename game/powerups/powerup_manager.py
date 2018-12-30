#################################################
# Powerup manager for all powerups in the game
# will spawn powerups, activate and update them
#################################################
import random
import math
from game.global_objects.constants import *
from game.misc.game_enums import E_Powerup_Type
from game.powerups import *


class Powerup_Manager(object):

    def __init__(self, spawn_cooldown, spawn_radius, powerup_expiry_duration, powerup_effect_duration):
        self.powerups = []
        self.timer = 0
        self.spawn_cooldown = spawn_cooldown
        self.spawn_radius = spawn_radius
        self.powerup_expiry_duration = powerup_expiry_duration
        self.powerup_effect_duration = powerup_effect_duration

    def update(self, delta_time):
        self.timer += delta_time

        if self.timer > self.spawn_cooldown:
            self.spawn_random_powerup()
            self.timer = 0

        for powerup in self.powerups:
            powerup.update(delta_time)

    def powerup_activated(self, powerup):
        pass

    def powerup_deactivated(self, powerup):
        pass

    def powerup_expired(self, powerup):
        pass

    def reset(self):
        self.powerups = []
        self.timer = 0
        pass

    def get_random_position(self):
        rand_angle = random.random() * 360
        rand_radius = random.random() * self.spawn_radius
        return(math.cos(rand_angle) * rand_radius, math.sin(rand_angle) * rand_radius)

    def spawn_random_powerup(self):
        rand = random.randint(0, 3)
        rand_pos = self.get_random_position()

        if rand == 0:
            powerup = Double_Damage_Powerup('Double Damage',
                                            'Increases damage',
                                            double_damage_powerup_img,
                                            powerup_img_radius,
                                            rand_pos[0],
                                            rand_pos[1],
                                            self.expire_duration,
                                            self.effect_duration,
                                            self)

        if rand == 0:
            powerup = Double_Power_Powerup('Double Power',
                                           'Increases hitting power',
                                           double_power_powerup_img,
                                           powerup_img_radius,
                                           rand_pos[0],
                                           rand_pos[1],
                                           self.expire_duration,
                                           self.effect_duration,
                                           self)

        if rand == 0:
            powerup = Double_Speed_Powerup('Double Speed',
                                           'Increases max speed',
                                           double_speed_powerup_img,
                                           powerup_img_radius,
                                           rand_pos[0],
                                           rand_pos[1],
                                           self.expire_duration,
                                           self.effect_duration,
                                           self)

        if rand == 0:
            powerup = No_Friction_Powerup('No Friction',
                                          'Remoes friction',
                                          no_friction_powerup_img,
                                          powerup_img_radius,
                                          rand_pos[0],
                                          rand_pos[1],
                                          self.expire_duration,
                                          self.effect_duration,
                                          self)

        self.powerups.append(powerup)
        # print(rand_powerup)
