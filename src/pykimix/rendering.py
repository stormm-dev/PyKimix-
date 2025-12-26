import sys
import random

try:
    import pygame
except ImportError:
    pygame = None

try:
    from kivy.graphics import Canvas as KivyCanvas
except ImportError:
    KivyCanvas = None

class Canvas:
    def __init__(self, width=800, height=600, backend="auto"):
        self.backend = backend
        if backend == "auto":
            if pygame:
                self.backend = "pygame"
            elif KivyCanvas:
                self.backend = "kivy"
        self.width = width
        self.height = height
        if self.backend == "pygame":
            pygame.display.init()
            self.screen = pygame.display.set_mode((width, height))
        else:
            self.screen = None

    def clear(self):
        if self.backend == "pygame":
            self.screen.fill((0, 0, 0))

    def draw_sprite(self, sprite, x, y):
        if self.backend == "pygame":
            self.screen.blit(sprite.image, (x, y))

    def present(self):
        if self.backend == "pygame":
            pygame.display.flip()