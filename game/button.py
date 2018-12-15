#######################################
# Easy to use buttons
#######################################
try:
    from .constants import *
except SystemError:
    from constants import *

class Button():
    def __init__(self, pygame, surface, rect, text, button_color, text_color):
        self.pygame = pygame
        self.surface = surface
        self.rect = self.pygame.Rect(rect)
        self.text = text
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.SysFont('cambria', 40)

    def draw(self):
        self.pygame.draw.rect(self.surface, self.button_color, self.rect)
        textsurface = self.font.render(self.text, True, self.text_color)
        self.surface.blit(textsurface, self.rect)

    def check_click(self, pos):
        return self.rect.collidepoint(pos)


class ImgButton():
    def __init__(self, pygame, surface, rect, image):
        self.pygame = pygame
        self.surface = surface
        self.rect = self.pygame.Rect(rect)
        self.image = pygame.transform.scale(image, (self.rect.w, self.rect.h))

    def draw(self):
        self.surface.blit(self.image, (self.rect.x, self.rect.y))

    def check_click(self, pos):
        return self.rect.collidepoint(pos)
