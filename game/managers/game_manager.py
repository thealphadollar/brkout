##################################################
# Game Manager
# Will hold reference of cross screen variables
# and game settings variables
####################################################


class Game_Manager():

    def __init__(self, pygame, screen, clock, settings_manager, sound_manager, animation_manager, game_parameters, input_manager, powerup_manager):
        self.pygame = pygame
        self.screen = screen
        self.clock = clock
        self.settings_manager = settings_manager
        self.sound_manager = sound_manager
        self.animation_manager = animation_manager
        self.game_parameters = game_parameters
        self.input_manager = input_manager
        self.powerup_manager = powerup_manager
