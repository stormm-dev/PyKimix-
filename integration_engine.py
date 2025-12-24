import time
import pygame
import platform
import os
from kivy.core.window import Window
from kivy.logger import Logger
from .utils import InputManager

# Suppress Kivy logs for Android
os.environ["KIVY_NO_CONSOLELOG"] = "1"
os.environ["KIVY_NO_FILELOG"] = "1"

class IntegrationEngine:
    def __init__(self, title="PyKimix Game", width=800, height=600, fps=60):
        pygame.init()
        self.title = title
        self.width = width
        self.height = height
        self.fps = fps
        self.sprites = []
        self.score = 0
        self.running = False

        # Modular input manager
        self.input = InputManager()

        # Android-safe: use surface instead of window
        if platform.system() == "Android":
            Logger.info(f"PyKimix: Running on Android, using offscreen surface ({width}x{height})")
            self.screen = pygame.Surface((width, height))
        else:
            self.screen = pygame.display.set_mode((width, height))
            pygame.display.set_caption(title)

        print(f"[IntegrationEngine] Initialized: {title} ({width}x{height})")

        # Callback lists
        self._update_callbacks = []
        self._draw_callbacks = []

    # Resource loading
    def load_image(self, path): 
        from .resources import load_image
        return load_image(path)

    def load_sound(self, path):
        from .resources import load_sound
        return load_sound(path)

    def load_font(self, path, size=24):
        from .resources import load_font
        return load_font(path, size)

    # Event callbacks
    def on_update(self, callback):
        self._update_callbacks.append(callback)

    def on_draw(self, callback):
        self._draw_callbacks.append(callback)

    # Sprite management
    def create_sprite(self, image, x=0, y=0):
        from .sprites import Sprite
        sprite = Sprite(image, x, y)
        self.sprites.append(sprite)
        return sprite

    def draw_sprite(self, sprite):
        from .gpu import draw_texture
        draw_texture(sprite.image, sprite.x, sprite.y)

    def clear_screen(self, color=(0,0,0)):
        from .gpu import clear_gpu_screen
        clear_gpu_screen(color)

    def draw_text(self, text, font, x, y, color=(255,255,255)):
        from .gpu import draw_text_gpu
        draw_text_gpu(text, font, x, y, color)

    # Music
    def play_music(self, music, loop=False):
        from .audio import MusicPlayer
        MusicPlayer.play(music, loop=loop)

    # Main loop
    def run(self):
        self.running = True
        dt = 1 / self.fps
        while self.running:
            start = time.time()

            # Pygame events -> InputManager
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    for cb in self.input.key_down_callbacks:
                        cb(event.key)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for cb in self.input.touch_callbacks:
                        cb(pos)

            # Call user update callbacks
            for callback in self._update_callbacks:
                callback(dt)

            # Call user draw callbacks
            for callback in self._draw_callbacks:
                callback()

            # Flip only on desktop
            if platform.system() != "Android":
                pygame.display.flip()

            elapsed = time.time() - start
            if elapsed < dt:
                time.sleep(dt - elapsed)