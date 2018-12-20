###############################################
# Sound Manager
# Controls music and sound effects
# Also mute and volume functions
###############################################
import os
from game.global_objects.constants import *

class Sound_Manager():

    def __init__(self, settings_manager, pygame):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        self.pygame = pygame
        self.settings_manager = settings_manager
        self.volume = self.settings_manager.settings_data['volume']
        self.mute = self.settings_manager.settings_data['mute']
        pass

    def mute_game(self):
        self.pygame.mixer.music.pause()
        self.settings_manager.settings_data['mute'] = True
        self.mute = True
        self.settings_manager.save_settings_to_file()

    def unmute_game(self):
        self.pygame.mixer.music.unpause()
        self.settings_manager.settings_data['mute'] = False
        self.mute = False
        self.settings_manager.save_settings_to_file()

    def change_volume(self, value):
        self.settings_manager.settings_data['volume'] = value
        self.volume = value
        self.settings_manager.save_settings_to_file()

    def play_music(self, name):
        self.pygame.mixer.music.stop()
        self.pygame.mixer.music.load(os.path.join(assets_directory, name))
        self.pygame.mixer.music.play(-1)
        self.pygame.mixer.music.set_volume(self.volume)

        if self.mute:
            self.pygame.mixer.music.pause()
