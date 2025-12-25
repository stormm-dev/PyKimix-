import os
import ctypes
import pygame
import sys
import random

try:
    from kivy import Config
    os.environ["KIVY_NO_MTDEV"] = "1"
    Config.set("kivy", "window", "sdl2")
    Config.set("kivy", "audio", "dummy")
except Exception:
    pass

def _auto_window_control():
    modules = sys.modules
    has_pygame = "pygame" in modules
    has_kivy = "kivy" in modules

    if not has_pygame and not has_kivy:
        return

    if has_pygame and has_kivy:
        close = random.choice(["pygame", "kivy"])
    elif has_pygame:
        close = "kivy"
    else:
        close = "pygame"

    if close == "pygame":
        try:
            pygame.display.quit()
            pygame.quit()
        except Exception:
            pass
    else:
        try:
            from kivy.app import App
            app = App.get_running_app()
            if app:
                app.stop()
        except Exception:
            pass

_auto_window_control()

_BASE_DIR = os.path.dirname(__file__)
_C_CORE_PATH = os.path.join(_BASE_DIR, "c_core", "libpykimix.so")

c_core = None
try:
    if os.path.exists(_C_CORE_PATH):
        c_core = ctypes.CDLL(_C_CORE_PATH)
except OSError:
    c_core = None

def add(a, b):
    if c_core:
        try:
            c_core.add.argtypes = [ctypes.c_int, ctypes.c_int]
            c_core.add.restype = ctypes.c_int
            return c_core.add(a, b)
        except Exception:
            pass
    return a + b

def sub(a, b):
    if c_core:
        try:
            c_core.sub.argtypes = [ctypes.c_int, ctypes.c_int]
            c_core.sub.restype = ctypes.c_int
            return c_core.sub(a, b)
        except Exception:
            pass
    return a - b

def mul(a, b):
    if c_core:
        try:
            c_core.mul.argtypes = [ctypes.c_int, ctypes.c_int]
            c_core.mul.restype = ctypes.c_int
            return c_core.mul(a, b)
        except Exception:
            pass
    return a * b

try:
    from .integration_engine import IntegrationEngine
except Exception:
    IntegrationEngine = None

try:
    from .resources import load_image, load_sound, load_font
except Exception:
    load_image = load_sound = load_font = None

try:
    from .sprites import Sprite
except Exception:
    Sprite = None

try:
    from .audio import MusicPlayer
except Exception:
    MusicPlayer = None

try:
    from .input import InputManager
except Exception:
    InputManager = None

try:
    from .gpu import GPU
except Exception:
    GPU = None

try:
    from .utils import *
except Exception:
    pass

_FONT_DIR = os.path.join(_BASE_DIR, "assets", "fonts")
_FONT_MAP = {}
for i, fname in enumerate(sorted(os.listdir(_FONT_DIR)), start=1):
    if fname.lower().endswith(".ttf"):
        _FONT_MAP[i] = fname

_FONT_CACHE = {}

def font(font_id, size=24, fallback=True):
    if not pygame.font.get_init():
        pygame.font.init()

    key = (font_id, size)
    if key in _FONT_CACHE:
        return _FONT_CACHE[key]

    filename = _FONT_MAP.get(font_id)
    if not filename:
        if fallback:
            return pygame.font.SysFont(None, size)
        raise ValueError(f"PyKimix font {font_id} not found")

    path = os.path.join(_FONT_DIR, filename)
    if not os.path.exists(path):
        if fallback:
            return pygame.font.SysFont(None, size)
        raise FileNotFoundError(path)

    f = pygame.font.Font(path, size)
    _FONT_CACHE[key] = f
    return f

def list_fonts():
    return list(_FONT_MAP.keys())

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

__version__ = "0.4.3"