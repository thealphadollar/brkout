###############################################
# Base class for all powerups
###############################################
from game.misc.collisions import Circle_Collider


class Powerup(object):

    def __init__(self, name, description, image, radius, pos_x, pos_y, duration, powerup_manager):
        self.name = name
        self.description = description
        self.image = image
        self.x = pos_x
        self.y = pos_y
        self.collider = Circle_Collider(self.x, self.y, radius)
        self.duration = duration
        self.powerup_manager = powerup_manager
        self.activated = False
        self.timer = 0

    def get_collider(self):
        return self.collider

    def check_collision(self, striker_collider):
        if self.activated:
            return
        
        pass

    def activate(self):
        pass

    def update(self, delta_time):
        self.timer += delta_time
        if self.timer > self.duration:
            self.expire()
        pass

    def expire(self):
        pass

    def deactivate(self):
        pass

    def draw(self, screen):
        if self.activated:
            return

        img_rect = self.ball_img_rotated.get_rect(center=(self.x, self.y))
        screen.blit(self.image, img_rect.topleft)
