#################################################
# Powerup manager for all powerups in the game
# will spawn powerups, activate and update them
#################################################


class Powerup_Manager(object):

    def __init__(self):
        self.powerups = []

    def spawn_random_powerup(self):
        pass

    def update_powerups(self, delta_time):
        for powerup in self.powerups:
            powerup.update(delta_time)

    def powerup_activated(self, powerup):
        pass

    def powerup_deactivated(self, powerup):
        pass

    def powerup_expired(self, powerup):
        pass
