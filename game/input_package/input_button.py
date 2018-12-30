#################################################
# An input that is controlled by a keypress
# Example: in a FPS game, key R to reload
# Buttons can be mapped to multiple keys
# Example: Reload can be done by key R or key E
# or a key on the joystick
#################################################

from .input_base import Input
import pygame.key


class Button(Input):

    def __init__(self, action_name, pygame_key_list):
        self.value = False
        self.action_name = action_name
        self.pygame_key_list = pygame_key_list

    def set_value(self, events, key_state):
        for key in self.pygame_key_list:
            if key_state[key]:
                self.value = 1
                return
