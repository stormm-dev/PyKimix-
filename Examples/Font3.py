import pygame
import pykimix
import os

pygame.init()
pygame.font.init()

info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h

try:
    pygame.display.quit()
except Exception:
    pass
pygame.display.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyKimix Font3 Test")

font_keys = pykimix.list_fonts()
if len(font_keys) >= 3:
    f = pykimix.font(3, 64)
else:
    f = pykimix.font(font_keys[-1], 64)

text = f.render("HELLO, WORLD!", True, (255, 255, 255))
text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    pygame.display.flip()

pygame.quit()
