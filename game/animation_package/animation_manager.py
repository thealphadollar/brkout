#########################################################
# Manager for the animation effect system.
# External systems will talk directly to the manager.
#########################################################

from .animation_effect import Animation_Effect


class Animation_Manager:
    def __init__(self, surface):
        ''' 
        Animation Manager constructor, sets surface, and initializes the animation effects list.
        :param surface: pygame surface to draw on.
        '''
        self.surface = surface
        self.animation_effects = []

    def create_new_effect(self, frames, frame_size, frame_length, looping=False, position=(0, 0)):
        '''
        Create a new animation effect
        :param frames: animation frames
        :param frame_size: size of animation
        :param frame_length: number of frames one animation frame will remain on screen
        :param looping: either loop the animation or stop on the last frame
        :param position: screen position of animation
        '''
        new_anim_effect = Animation_Effect(
            self, self.surface, frames, frame_size, frame_length, looping, position)
        self.animation_effects.append(new_anim_effect)

    def draw_animations(self):
        ''' Draw all the animation in the list. '''
        for animation_effect in self.animation_effects:
            animation_effect.draw()

    def remove_animation_effect(self, animation_effect):
        ''' Internal function to remove any animation effect from the list, that has finished playing. '''
        self.animation_effects.remove(animation_effect)
