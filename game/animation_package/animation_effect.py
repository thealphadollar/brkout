################################################
# Class for showing animation effects on screen
# can be spawned on screen and
# will either die after one loop or stay there
################################################

from .animation import Animation


class Animation_Effect:
    def __init__(self, animation_manager, surface, frames, frame_size, frame_length, looping=False, position=(0, 0)):
        self.animation_manager = animation_manager
        self.animation = Animation(self, surface, frames, frame_size, frame_length, looping)
        self.position = position

    def move(self, new_position):
        self.position = new_position

    def draw(self):
        self.animation.draw(self.position)

    def animation_over(self):
        self.animation_manager.remove_animation_effect(self)
