import os
import sys
import ctypes
import random
import pygame

if "_PYKIMIX_LOADED" in globals():
    pass
else:
    _PYKIMIX_LOADED = True


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
        close = random.choice(("pygame", "kivy"))
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
except Exception:
    c_core = None


def _bind(name, restype, *argtypes):
    if not c_core:
        return None
    try:
        fn = getattr(c_core, name)
        fn.restype = restype
        fn.argtypes = list(argtypes)
        return fn
    except Exception:
        return None


_c_add = _bind("pyk_add", ctypes.c_int, ctypes.c_int, ctypes.c_int)
_c_sub = _bind("pyk_sub", ctypes.c_int, ctypes.c_int, ctypes.c_int)
_c_mul = _bind("pyk_mul", ctypes.c_int, ctypes.c_int, ctypes.c_int)
_c_rand = _bind("pyk_random_int", ctypes.c_int, ctypes.c_int, ctypes.c_int)
_c_gpu_init = _bind("pyk_gpu_init", None)
_c_gpu_shutdown = _bind("pyk_gpu_shutdown", None)


def add(a, b):
    return _c_add(a, b) if _c_add else a + b


def sub(a, b):
    return _c_sub(a, b) if _c_sub else a - b


def mul(a, b):
    return _c_mul(a, b) if _c_mul else a * b


def random_int(a, b):
    return _c_rand(a, b) if _c_rand else random.randint(a, b)


class GPU:
    def __init__(self):
        if _c_gpu_init:
            _c_gpu_init()

    def shutdown(self):
        if _c_gpu_shutdown:
            _c_gpu_shutdown()


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
    from .utils import *
except Exception:
    pass


_FONT_DIR = os.path.join(_BASE_DIR, "assets", "fonts")
_FONT_MAP = {}
_FONT_CACHE = {}

if os.path.isdir(_FONT_DIR):
    for i, fname in enumerate(sorted(os.listdir(_FONT_DIR)), start=1):
        if fname.lower().endswith(".ttf"):
            _FONT_MAP[i] = fname


def font(font_id, size=24, fallback=True):
    if not pygame.font.get_init():
        pygame.font.init()

    key = (font_id, size)
    if key in _FONT_CACHE:
        return _FONT_CACHE[key]

    filename = _FONT_MAP.get(font_id)
    if not filename:
        return pygame.font.SysFont(None, size) if fallback else None

    path = os.path.join(_FONT_DIR, filename)
    if not os.path.exists(path):
        return pygame.font.SysFont(None, size) if fallback else None

    f = pygame.font.Font(path, size)
    _FONT_CACHE[key] = f
    return f


def list_fonts():
    return list(_FONT_MAP.keys())


def capabilities():
    return {
        "native": c_core is not None,
        "pygame": "pygame" in sys.modules,
        "kivy": "kivy" in sys.modules,
    }


def _engine_init():
    pass


_engine_init()


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
    "random_int",
    "capabilities",
]


__version__ = "0.4.31"
__abi_version__ = 1
__author__ = "stormm-dev"
__license__ = "MIT"
__repo__ = "https://github.com/stormm-dev/pykimix"
__pykimix_native__ = c_core is not None