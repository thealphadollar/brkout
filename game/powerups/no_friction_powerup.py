##########################################
# Removes friction temporarily
##########################################
from .powerup import Powerup
from game.global_objects.constants import *


class No_Friction_Powerup(Powerup):

    def __init__(self, pos_x, pos_y, radius, expire_duration, effect_duration, powerup_manager):
        super().__init__(pos_x, pos_y, radius, expire_duration,
                         effect_duration, powerup_manager)
        self.name = 'No Friction'
        self.description = 'Removes friction'
        self.image = no_friction_powerup_img

    def activate(self):
        self.old_value = self.powerup_manager.run_vars.friction
        self.powerup_manager.run_vars.friction = 0.0
        self.activated = True

    def deactivate(self):
        self.powerup_manager.run_vars.friction = self.old_value
        self.powerup_manager.powerup_deactivated(self)
