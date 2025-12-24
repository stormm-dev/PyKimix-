import pygame
import time

class InputManager:
    def __init__(self):
        self.key_down_callbacks = []
        self.key_up_callbacks = []
        self.touch_callbacks = []
        self.mouse_motion_callbacks = []

    def register_key_down(self, callback):
        self.key_down_callbacks.append(callback)

    def register_key_up(self, callback):
        self.key_up_callbacks.append(callback)

    def register_touch(self, callback):
        self.touch_callbacks.append(callback)

    def register_mouse_motion(self, callback):
        self.mouse_motion_callbacks.append(callback)

class Timer:
    def __init__(self):
        self.timers = []

    def schedule(self, delay, callback):
        execute_at = time.time() + delay
        self.timers.append((execute_at, callback))

    def update(self):
        now = time.time()
        for timer in self.timers[:]:
            execute_at, callback = timer
            if now >= execute_at:
                callback()
                self.timers.remove(timer)

def lerp(a, b, t):
    return a + (b - a) * t

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))

def screen_to_world(x, y, camera_x=0, camera_y=0):
    return x + camera_x, y + camera_y