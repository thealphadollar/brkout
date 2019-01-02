from .powerup import Powerup
from game.global_objects.constants import *


class No_Friction_Powerup(Powerup):

    def __init__(self, pos_x, pos_y, radius, expire_duration, effect_duration, powerup_manager):
        super().__init__(pos_x, pos_y, radius, expire_duration,
                         effect_duration, powerup_manager)
        self.name = 'No Friction'
        self.description = 'Removes friction'
        self.image = no_friction_powerup_img
