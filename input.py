import pygame

class InputManager:
    def __init__(self):
        """Initialize input system."""
        self.keys_pressed = []
        self.touch_pos = None
        try:
            pygame.init()
            pygame.joystick.init()
        except Exception as e:
            print("Pygame input initialization skipped:", e)

    def update(self):
        """Update the input states."""
        try:
            pygame.event.pump()
            self.keys_pressed = [i for i, k in enumerate(pygame.key.get_pressed()) if k]
        except:
            self.keys_pressed = []

    def get_keys(self):
        """Return currently pressed keys."""
        return self.keys_pressed

    def get_touch(self):
        """Return touch/mouse position (currently None)."""
        return self.touch_pos