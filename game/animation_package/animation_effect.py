################################################
# Class for showing animation effects on screen
# can be spawned on screen and
# will either die after one loop or stay there
################################################

from .animation import Animation


class Animation_Effect:
    def __init__(self, animation_manager, surface, frames, frame_size, frame_length, looping=False, position=(0, 0)):
        '''
        Animation effect constructor
        :param animation_manager: manager
        :param surface: pygame surface
        :param frames: animation frames
        :param frame_size: size of animation
        :param frame_length: number of frames one animation frame will remain on screen
        :param looping: either loop the animation or stop on the last frame
        :param position: screen position of animation
        '''
        self.animation_manager = animation_manager
        self.animation = Animation(
            self, surface, frames, frame_size, frame_length, looping)
        self.position = position

    def move(self, new_position):
        ''' Move animation effect on screen. '''
        self.position = new_position

    def draw(self):
        ''' Draw animation effect on screen. '''
        self.animation.draw(self.position)

    def animation_over(self):
        ''' Called by animation when looping is False. '''
        self.animation_manager.remove_animation_effect(self)
