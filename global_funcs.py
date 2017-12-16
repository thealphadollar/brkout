# this file contains functions for global use
import pygame

# function to render font


def text_obj(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()

# function to display text


def disp_text(screen, text, center, font_and_size, color):
    text_surf, text_rect = text_obj(text, font_and_size, color)
    text_rect.center = center
    screen.blit(text_surf, text_rect)


