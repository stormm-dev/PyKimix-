import pygame

def draw_texture(image, x, y):
    print(f"[GPU] Drawing texture at ({x},{y})")

def clear_gpu_screen(color=(0,0,0)):
    print(f"[GPU] Clearing screen with color {color}")

def draw_text_gpu(text, font, x, y, color=(255,255,255)):
    print(f"[GPU] Drawing text '{text}' at ({x},{y}) color={color}")