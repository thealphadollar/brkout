import pygame
import os
import sys

# function to render font


def textObj (text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

# function to display text
def dispText(screen, text, center, fontAndSize, color):
    TextSurf, TextRect = textObj(text, fontAndSize, color)
    TextRect.center = center
    screen.blit(TextSurf, TextRect)




