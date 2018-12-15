########################################################
# Class for animation
# animation is a set of images to be played in sequence
########################################################


class Animation:
    def __init__(self, parent, surface, frames, frame_size, frame_length, looping=False):
        self.parent = parent
        self.surface = surface
        self.frames = frames
        self.frame_size = frame_size
        self.frame_length = 10
        self.looping = looping
        self.frame_index = 0
        self.frame_counter = 0

    def reset_animation(self):
        self.frame_index = 0
        self.frame_counter = 0

    def draw(self, position=(0, 0)):
        self.surface.blit(self.frames[self.frame_index], self.offset_position(position))
        self.advance_animation()

    def advance_animation(self):
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
        return (position[0] - (self.frame_size / 2), position[1] - (self.frame_size / 2))
