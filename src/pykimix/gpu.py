import os
import sys
import ctypes

_BASE_DIR = os.path.dirname(__file__)

if sys.platform.startswith("win"):
    _GPU_CORE = os.path.join(_BASE_DIR, "c_core", "libpykimix.dll")
else:
    _GPU_CORE = os.path.join(_BASE_DIR, "c_core", "libpykimix.so")

_gpu = None
try:
    _gpu = ctypes.CDLL(_GPU_CORE)
except Exception:
    _gpu = None


class CSprite(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int),
        ("w", ctypes.c_int),
        ("h", ctypes.c_int),
        ("pixels", ctypes.POINTER(ctypes.c_uint32)),
    ]


class GPU:
    def __init__(self, surface):
        self.surface = surface
        self.width, self.height = surface.get_size()

        if _gpu:
            _gpu.draw_sprite.argtypes = [
                ctypes.POINTER(ctypes.c_uint32),
                ctypes.c_int,
                ctypes.c_int,
                ctypes.POINTER(CSprite),
            ]
            _gpu.draw_sprite.restype = None

    def draw_sprite(self, sprite, x, y):
        sprite_rect = sprite.get_rect(topleft=(x, y))

        if _gpu:
            buf = self.surface.get_buffer()
            buf_ptr = ctypes.cast(
                buf.raw, ctypes.POINTER(ctypes.c_uint32)
            )

            pixels = sprite.get_buffer()
            pix_ptr = ctypes.cast(
                pixels.raw, ctypes.POINTER(ctypes.c_uint32)
            )

            c_sprite = CSprite(
                x,
                y,
                sprite_rect.width,
                sprite_rect.height,
                pix_ptr,
            )

            _gpu.draw_sprite(
                buf_ptr,
                self.width,
                self.height,
                ctypes.byref(c_sprite),
            )
        else:
            self.surface.blit(sprite, (x, y))