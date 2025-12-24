import pygame

class Sprite:
    def __init__(self, image, x=0, y=0):
        """
        image: pygame.Surface or Kivy-compatible texture
        x, y: position
        """
        self.image = image
        self.x = x
        self.y = y
        self.visible = True

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def collides_with(self, other):
        """Basic collision check using bounding boxes (50x50 default)"""
        return abs(self.x - other.x) < 50 and abs(self.y - other.y) < 50

    def draw(self, surface):
        """Draw the sprite on a given Pygame surface"""
        if self.visible and isinstance(self.image, pygame.Surface):
            surface.blit(self.image, (self.x, self.y))