import pygame
from kivy.core.audio import SoundLoader

def load_image(path):
    print(f"[Resources] Loaded image: {path}")
    return pygame.Surface((50,50))  # placeholder surface

def load_sound(path):
    print(f"[Resources] Loaded sound: {path}")
    return SoundLoader.load(path)

def load_font(path, size):
    print(f"[Resources] Loaded font: {path} size={size}")
    return {"path": path, "size": size}  # placeholder font dict