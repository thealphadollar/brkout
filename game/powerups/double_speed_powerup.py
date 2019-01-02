from .powerup import Powerup
from game.global_objects.constants import *


class Double_Speed_Powerup(Powerup):

    def __init__(self, pos_x, pos_y, radius, expire_duration, effect_duration, powerup_manager):
        super().__init__(pos_x, pos_y, radius, expire_duration,
                         effect_duration, powerup_manager)
        self.name = 'Double Speed'
        self.description = 'Increases max speed'
        self.image = double_speed_powerup_img
