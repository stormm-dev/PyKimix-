import math
from .core import add, sub, mul

def clamp(val, min_val, max_val):
    return max(min_val, min(val, max_val))

def lerp(a, b, t):
    """Linear interpolation, can be moved to C core later"""
    return a + (b - a) * t

def distance(x1, y1, x2, y2):
    dx = sub(x2, x1)
    dy = sub(y2, y1)
    return math.sqrt(dx*dx + dy*dy)