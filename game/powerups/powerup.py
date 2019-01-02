###############################################
# Base class for all powerups
###############################################
from game.misc.collisions import Circle_Collider
from game.misc.collisions import Collision


class Powerup(object):

    def __init__(self, pos_x, pos_y, radius, expire_duration, effect_duration, powerup_manager):
        self.name = 'Powerup'
        self.description = 'Description'
        self.image = None
        self.radius = radius
        self.x = pos_x
        self.y = pos_y
        self.collider = Circle_Collider(self.x, self.y, self.radius)
        self.expire_duration = expire_duration
        self.effect_duration = effect_duration
        self.powerup_manager = powerup_manager
        self.activated = False
        self.expire_timer = 0
        self.effect_timer = 0

    def get_collider(self):
        return self.collider

    def check_collision(self, striker_collider):
        if self.activated:
            return

        collision = Collision.check(self.collider, striker_collider)
        if collision != (0, 0):
            self.activate()

    def activate(self):
        self.activated = True

    def update(self, delta_time):
        if not self.activated:
            self.expire_timer += delta_time
            if self.expire_timer > self.expire_duration:
                self.expire()
        else:
            self.effect_timer += delta_time
            if self.effect_timer > self.effect_duration:
                self.deactivate()

    def expire(self):
        self.powerup_manager.powerup_expired(self)

    def deactivate(self):
        self.powerup_manager.powerup_deactivated(self)

    def draw(self, screen):
        if self.activated:
            return

        img_rect = self.image.get_rect(center=(self.x, self.y))
        screen.blit(self.image, img_rect.topleft)
