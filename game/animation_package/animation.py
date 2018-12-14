########################################################
# Class for animation
# animation is a set of images to be played in sequence
########################################################


class Animation:
    def __init__(self, surface, frames, frame_length, looping=False):
        self.surface = surface
        self.frames = frames
        self.frame_length = 10
        self.looping = looping
        self.frame_index = 0
        self.frame_counter = 0

    def reset_animation(self):
        self.frame_index = 0
        self.frame_counter = 0

    def draw(self, position=(0, 0)):
        self.surface.blit(self.frames[self.frame_index], position)
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
