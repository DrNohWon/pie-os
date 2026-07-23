import os
import pygame
import time

# Tell SDL to use framebuffer
os.environ["SDL_VIDEODRIVER"] = "fbcon"
os.environ["SDL_FBDEV"] = "/dev/fb1"

pygame.init()

screen = pygame.display.set_mode((480,320))

font = pygame.font.Font(None,50)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            running = False

    screen.fill((0,0,0))

    text = font.render(
        "P.I.E.",
        True,
        (0,255,0)
    )

    screen.blit(
        text,
        (160,130)
    )

    pygame.display.update()

    time.sleep(0.1)

pygame.quit()
