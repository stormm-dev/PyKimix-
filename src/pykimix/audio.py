import pygame
pygame.mixer.init()

class MusicPlayer:
    @staticmethod
    def play(sound, loop=False):
        """
        Plays a pygame or Kivy sound object.
        If it's a pygame.mixer.Sound: use pygame
        If it's a Kivy SoundLoader object: use its play method
        """
        try:
            # For Kivy SoundLoader object
            sound.play()
        except AttributeError:
            # For pygame Sound object
            if isinstance(sound, pygame.mixer.Sound):
                loops = -1 if loop else 0
                sound.play(loops=loops)
        print(f"[Audio] Playing sound {getattr(sound, 'name', str(sound))} loop={loop}")