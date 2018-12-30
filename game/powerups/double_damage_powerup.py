from .powerup import Powerup


class Double_Damage_Powerup(Powerup):

    def __init__(self, name, description, image, radius, pos_x, pos_y, expire_duration, effect_duration, powerup_manager)):
        super(Powerup, self).__init__(self, name, description, image, radius, pos_x, pos_y, expire_duration, effect_duration, powerup_manager))
