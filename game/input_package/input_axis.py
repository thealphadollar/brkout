##############################################################################
# An input that is controlled by two keys and can have 3 values, -1, 0, 1
#
# Example: in a FPS game, keys W and S control forward and backward movement
#
#   pressing W,        output is +1 or move forward
#   pressing S,        output is -1 or move backward
#   pressing nothing,  output is 0 or don't move
##############################################################################

from .input_base import Input
import pygame.key


class Axis(Input):

    def __init__(self, action_name, pygame_key_pair_list):
        self.value = 0
        self.action_name = action_name
        self.pygame_key_pair_list = pygame_key_pair_list

    def set_value(self, events, key_state):
        for key_pair in self.pygame_key_pair_list:
            negative_key, positive_key = key_pair
            if key_state[negative_key]:
                self.value += -1
                if self.value < -1:
                    self.value = -1

            if key_state[positive_key]:
                self.value += 1
                if self.value > 1:
                    self.value = 1
