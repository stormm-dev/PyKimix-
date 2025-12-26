import pygame

class InputManager:
    def __init__(self):
        self.keys_down = set()
        self.touch_events = []

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.keys_down.add(event.key)
            if event.type == pygame.KEYUP:
                self.keys_down.discard(event.key)

    def key_down(self, key_name):
        return getattr(pygame, f"K_{key_name.upper()}", None) in self.keys_down