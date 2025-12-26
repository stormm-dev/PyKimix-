import ctypes
import os

_BASE_DIR = os.path.dirname(__file__)
_C_CORE_PATH = os.path.join(_BASE_DIR, "c_core", "libpykimix.so")

c_core = None
try:
    c_core = ctypes.CDLL(_C_CORE_PATH)
except Exception:
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