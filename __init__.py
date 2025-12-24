import os
from kivy import Config
import pygame
import ctypes

# --- Kivy config ---
os.environ["KIVY_NO_MTDEV"] = "1"
Config.set("kivy", "window", "sdl2")
Config.set("kivy", "audio", "dummy")

# --- Load C core ---
_BASE_DIR = os.path.dirname(__file__)
_C_CORE_PATH = os.path.join(_BASE_DIR, "c_core", "libpykimix.so")  # .dll for Windows
try:
    c_core = ctypes.CDLL(_C_CORE_PATH)
except OSError:
    c_core = None
    print("Warning: C core not found, falling back to Python functions")

# --- Python wrappers for C functions ---
def add(a, b):
    if c_core:
        c_core.add.argtypes = [ctypes.c_int, ctypes.c_int]
        c_core.add.restype = ctypes.c_int
        return c_core.add(a, b)
    return a + b  # fallback

def sub(a, b):
    if c_core:
        c_core.sub.argtypes = [ctypes.c_int, ctypes.c_int]
        c_core.sub.restype = ctypes.c_int
        return c_core.sub(a, b)
    return a - b

def mul(a, b):
    if c_core:
        c_core.mul.argtypes = [ctypes.c_int, ctypes.c_int]
        c_core.mul.restype = ctypes.c_int
        return c_core.mul(a, b)
    return a * b

# --- Python modules ---
from .integration_engine import IntegrationEngine
from .resources import load_image, load_sound, load_font
from .sprites import Sprite
from .audio import MusicPlayer
from .input import InputManager
from .gpu import GPU
from .utils import *

# --- Font system ---
_FONT_DIR = os.path.join(_BASE_DIR, "assets", "fonts")
_FONT_MAP = {1: "font1.ttf"}
_FONT_CACHE = {}

def font(font_id, size=24, fallback=True):
    if not pygame.font.get_init():
        pygame.font.init()
    key = (font_id, size)
    if key in _FONT_CACHE:
        return _FONT_CACHE[key]
    if font_id not in _FONT_MAP:
        if fallback:
            return pygame.font.SysFont(None, size)
        raise ValueError(f"pykimix font {font_id} not found")
    path = os.path.join(_FONT_DIR, _FONT_MAP[font_id])
    f = pygame.font.Font(path, size)
    _FONT_CACHE[key] = f
    return f

def list_fonts():
    return list(_FONT_MAP.keys())

# --- Public API ---
__all__ = [
    "IntegrationEngine",
    "load_image",
    "load_sound",
    "load_font",
    "Sprite",
    "MusicPlayer",
    "InputManager",
    "GPU",
    "font",
    "list_fonts",
    "add",
    "sub",
    "mul",
]

__version__ = "0.4.1"