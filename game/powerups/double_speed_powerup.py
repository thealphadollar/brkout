##########################################
# Damage maximum speed for ball
##########################################
from .powerup import Powerup
from game.global_objects.constants import *


class Double_Speed_Powerup(Powerup):

    def __init__(self, pos_x, pos_y, radius, expire_duration, effect_duration, powerup_manager):
        super().__init__(pos_x, pos_y, radius, expire_duration,
                         effect_duration, powerup_manager)
        self.name = 'Double Speed'
        self.description = 'Increases max speed'
        self.image = double_speed_powerup_img

    def activate(self):
        self.old_value = self.powerup_manager.run_vars.ball_max_speed
        self.powerup_manager.run_vars.ball_max_speed = self.old_value * 2.0
        self.activated = True

    def deactivate(self):
        self.powerup_manager.run_vars.ball_max_speed = self.old_value
        self.powerup_manager.powerup_deactivated(self)
