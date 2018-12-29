#################################################
# An input that is controlled by a keypress up
# Example: in a FPS game, key R to reload
# Buttons can be mapped to multiple keys
# Example: Reload can be done by key R or key E
# or a key on the joystick
#################################################

from .input_base import Input
import pygame.key


class Button_Up(Input):

    def __init__(self, action_name, pygame_key_list):
        self.value = False
        self.action_name = action_name
        self.pygame_key_list = pygame_key_list

    def reset_value(self):
        self.value = False

    def set_value(self, events, key_state):
        self.value = False

        for event in events:
            for key in self.pygame_key_list:
                if event.type == pygame.KEYUP and event.key == key:
                    self.value = 1
                    return
