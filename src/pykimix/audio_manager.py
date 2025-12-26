import pygame
import threading

class AudioManager:
    def __init__(self):
        if pygame.mixer.get_init() is None:
            pygame.mixer.init()
        self.channels = {}
        self.music_channel = pygame.mixer.Channel(0)

    def play_sound(self, path):
        sound = pygame.mixer.Sound(path)
        pygame.mixer.find_channel(True).play(sound)

    def play_music(self, path, fadein=0):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1, fade_ms=fadein)

    def set_volume(self, vol):
        pygame.mixer.music.set_volume(vol)

    def crossfade(self, path, duration=1000):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1, fade_ms=duration)