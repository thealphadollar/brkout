##########################################################
# Class for animation.
# Animation is a set of images to be played in sequence.
##########################################################


class Animation:
    def __init__(self, parent, surface, frames, frame_size, frame_length, looping=False):
        '''
        Animation constructor
        :param parent: the animation effect which this belongs to
        :param surface: pygame surface where it's drawn
        :param frames: animation frames
        :param frame_size: size of animation
        :param frame_length: number of frames one animation frame will remain on screen
        :param looping: either loop the animation or stop on the last frame
        '''
        self.parent = parent
        self.surface = surface
        self.frames = frames
        self.frame_size = frame_size
        self.frame_length = 10
        self.looping = looping
        self.frame_index = 0
        self.frame_counter = 0

    def reset_animation(self):
        ''' Resets the animtions, will start from the first frame. '''
        self.frame_index = 0
        self.frame_counter = 0

    def draw(self, position=(0, 0)):
        ''' 
        Draw the animation frame
        :param position: screen position
        '''
        self.surface.blit(
            self.frames[self.frame_index], self.offset_position(position))
        self.advance_animation()

    def advance_animation(self):
        ''' Move to the next animation frame, or loop back if necessary. '''
        self.frame_counter += 1

        if self.frame_counter > self.frame_length:
            self.frame_counter = 0
            self.frame_index += 1

            if self.frame_index >= len(self.frames):
                if self.looping:
                    self.frame_index = 0
                else:
                    self.frame_index = len(self.frames) - 1
                    self.parent.animation_over()

    def offset_position(self, position):
        ''' 
        pygame origin is at top left of image, while animation is drawn from center
            this offsets that. 
        :param position: old position in top left coordinate system
        :return: new position in center coordinate system
        '''
        return (position[0] - (self.frame_size / 2), position[1] - (self.frame_size / 2))
