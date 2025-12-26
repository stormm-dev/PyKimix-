import os
import pygame

_BASE_DIR = os.path.dirname(__file__)
_ASSET_DIR = os.path.join(_BASE_DIR, "assets")

_image_cache = {}
_sound_cache = {}
_font_cache = {}

def load_image(name):
    path = os.path.join(_ASSET_DIR, "images", name)
    if path not in _image_cache:
        _image_cache[path] = pygame.image.load(path).convert_alpha()
    return _image_cache[path]

def load_sound(name):
    path = os.path.join(_ASSET_DIR, "sounds", name)
    if path not in _sound_cache:
        _sound_cache[path] = pygame.mixer.Sound(path)
    return _sound_cache[path]

def load_font(name, size=24):
    path = os.path.join(_ASSET_DIR, "fonts", name)
    key = (path, size)
    if key not in _font_cache:
        _font_cache[key] = pygame.font.Font(path, size)
    return _font_cache[key]