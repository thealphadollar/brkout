##########################################
# Damage done to bricks is doubled
##########################################
from .powerup import Powerup
from game.global_objects.constants import *


class Double_Damage_Powerup(Powerup):

    def __init__(self, pos_x, pos_y, radius, expire_duration, effect_duration, powerup_manager):
        super().__init__(pos_x, pos_y, radius, expire_duration,
                         effect_duration, powerup_manager)
        self.name = 'Double Damage'
        self.description = 'Increases damage'
        self.image = double_damage_powerup_img

    def activate(self):
        self.old_value = self.powerup_manager.run_vars.damage_multiplier
        self.powerup_manager.run_vars.damage_multiplier = self.old_value * 2
        self.activated = True

    def deactivate(self):
        self.powerup_manager.run_vars.damage_multiplier = self.old_value
        self.powerup_manager.powerup_deactivated(self)
