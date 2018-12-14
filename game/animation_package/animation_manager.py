#########################################################
# Manager for the animation effect system
#########################################################

from .animation_effect import Animation_Effect


class Animation_Manager:
    def __init__(self, surface):
        self.surface = surface
        self.animation_effects = []

    def create_new_effect(self, frames, frame_size, frame_length, looping=False, position=(0, 0)):
        new_anim_effect = Animation_Effect(
            self, self.surface, frames, frame_size, frame_length, looping, position)
        self.animation_effects.append(new_anim_effect)

    def draw_animations(self):
        for animation_effect in self.animation_effects:
            animation_effect.draw()

    def remove_animation_effect(self, animation_effect):
        self.animation_effects.remove(animation_effect)
