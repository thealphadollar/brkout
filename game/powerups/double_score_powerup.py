from .powerup import Powerup
from game.global_objects.constants import *


class Double_Score_Powerup(Powerup):

    def __init__(self, pos_x, pos_y, radius, expire_duration, effect_duration, powerup_manager):
        super().__init__(pos_x, pos_y, radius, expire_duration,
                         effect_duration, powerup_manager)
        self.name = 'Double Score'
        self.description = 'Get double score'
        self.image = double_score_powerup_img

    def activate(self):
        self.old_value = self.powerup_manager.run_vars.score_multiplier
        self.powerup_manager.run_vars.score_multiplier = self.old_value * 2.0
        self.activated = True

    def deactivate(self):
        self.powerup_manager.run_vars.score_multiplier = self.old_value
        self.powerup_manager.powerup_deactivated(self)
