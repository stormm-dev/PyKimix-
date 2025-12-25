import sys
import random

def _auto_window_control():
    modules = sys.modules

    has_pygame = "pygame" in modules
    has_kivy = "kivy" in modules

    if not has_pygame and not has_kivy:
        return  # Nothing to do

    # Decide which window to close
    if has_pygame and has_kivy:
        close = random.choice(["pygame", "kivy"])
    elif has_pygame:
        close = "kivy"
    else:
        close = "pygame"

    # Close safely
    if close == "pygame":
        try:
            import pygame
            pygame.display.quit()
            pygame.quit()
        except Exception:
            pass
    elif close == "kivy":
        try:
            from kivy.app import App
            app = App.get_running_app()
            if app:
                app.stop()
        except Exception:
            pass