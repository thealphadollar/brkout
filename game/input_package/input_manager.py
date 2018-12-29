###############################################################
# Manages input
# Will act as a wrapper around the pygame input functionality
# and provide ease of use for common input tasks
# Will support:
#   multiple keys for same action
#   axis input (three possible input: -1, 0, 1)
#   joystick input
#
# Define your input scheme at input_scheme.py
###############################################################

from .input_button import Button
from .input_axis import Axis
from .input_scheme import *
import pygame.key


class Input_Manager():
    '''
    Will have the states of all the buttons and axis defined by the game.
    These states can be retrieved from here with simple functions
    Will get these states at the start of the frame
    '''

    def __init__(self):
        self.input_list = get_input_list()

    def update(self, events):
        # read the keyboard for processing
        pygame.event.pump()
        key_state = pygame.key.get_pressed()

        # reset all the values from last frame
        for dict_key in self.input_list:
            self.input_list[dict_key].reset_value()

        # handle the key state
        self.handle_keyboard(events, key_state)

    def get_button(self, button_name):
        '''
        Gets the state of a user defined button
        :param button_name: the button name as defined in input_scheme
        :return True if button is pressed down state, False otherwise
        '''

        return self.input_list[button_name].get_value()

    def get_axis(self, axis_name):
        '''
        Get the value of a user defined axis
        :param axis_name: the axis name as defined in input_scheme
        :return -1 if negative key is pressed
                 0 if nothing is pressed
                 1 if positive key is pressed
        '''
        return self.input_list[axis_name].get_value()

    def handle_keyboard(self, events, key_state):
        for key in self.input_list:
            self.input_list[key].set_value(events, key_state)

    def handle_mouse_event(self, evnet):
        pass
