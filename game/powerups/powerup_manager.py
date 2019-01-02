#################################################
# Powerup manager for all powerups in the game
# will spawn powerups, activate and update them
#################################################
import random
import math
from game.global_objects.constants import *
from game.global_objects.global_funcs import disp_text
from game.misc.game_enums import E_Powerup_Type
from game.powerups import *


class Powerup_Manager(object):

    def __init__(self, screen, spawn_cooldown, spawn_radius, powerup_expiry_duration, powerup_effect_duration):
        self.screen = screen
        self.powerups = []
        self.timer = 0
        self.spawn_cooldown = spawn_cooldown
        self.spawn_radius = spawn_radius
        self.powerup_expiry_duration = powerup_expiry_duration
        self.powerup_effect_duration = powerup_effect_duration

    def update(self, delta_time, striker_collider):
        self.timer += delta_time

        if self.timer > self.spawn_cooldown:
            self.spawn_random_powerup()
            self.timer = 0

        for powerup in self.powerups:
            powerup.check_collision(striker_collider)
            powerup.update(delta_time)

    def draw(self):
        i = 0
        for powerup in self.powerups:
            powerup.draw(self.screen)
            if powerup.activated:
                i += 1
                disp_text(self.screen, powerup.name,
                          (250, 15 * i), message_text, white)

    def powerup_activated(self, powerup):
        pass

    def powerup_deactivated(self, powerup):
        self.powerups.remove(powerup)

    def powerup_expired(self, powerup):
        self.powerups.remove(powerup)

    def reset(self, run_vars):
        self.powerups = []
        self.timer = 0
        self.run_vars = run_vars

    def get_random_position(self):
        rand_angle = random.random() * 360
        rand_radius = random.random() * self.spawn_radius
        return(main_game_middle_x + math.cos(rand_angle) * rand_radius, main_game_middle_y + math.sin(rand_angle) * rand_radius)

    def spawn_random_powerup(self):
        rand = random.randint(0, len(E_Powerup_Type) - 1)
        rand_powerup = E_Powerup_Type(rand)
        rand_powerup = E_Powerup_Type.no_friction
        rand_pos = self.get_random_position()

        if rand_powerup == E_Powerup_Type.double_damage:
            powerup = Double_Damage_Powerup(rand_pos[0],
                                            rand_pos[1],
                                            powerup_collider_radius,
                                            self.powerup_expiry_duration,
                                            self.powerup_effect_duration,
                                            self)

        if rand_powerup == E_Powerup_Type.double_power:
            powerup = Double_Power_Powerup(rand_pos[0],
                                           rand_pos[1],
                                           powerup_collider_radius,
                                           self.powerup_expiry_duration,
                                           self.powerup_effect_duration,
                                           self)

        if rand_powerup == E_Powerup_Type.double_speed:
            powerup = Double_Speed_Powerup(rand_pos[0],
                                           rand_pos[1],
                                           powerup_collider_radius,
                                           self.powerup_expiry_duration,
                                           self.powerup_effect_duration,
                                           self)

        if rand_powerup == E_Powerup_Type.no_friction:
            powerup = No_Friction_Powerup(rand_pos[0],
                                          rand_pos[1],
                                          powerup_collider_radius,
                                          self.powerup_expiry_duration,
                                          self.powerup_effect_duration,
                                          self)

        if rand_powerup == E_Powerup_Type.double_score:
            powerup = Double_Score_Powerup(rand_pos[0],
                                           rand_pos[1],
                                           powerup_collider_radius,
                                           self.powerup_expiry_duration,
                                           self.powerup_effect_duration,
                                           self)

        self.powerups.append(powerup)
