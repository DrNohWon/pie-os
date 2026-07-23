"""
P.I.E. Renderer

Basic drawing primitives.
"""

import pygame


class Renderer:


    def __init__(self, surface):

        self.surface = surface



    def clear(self, color):

        self.surface.fill(
            color
        )



    def text(
        self,
        text,
        position,
        font,
        color
    ):

        image = font.render(
            text,
            True,
            color
        )

        self.surface.blit(
            image,
            position
        )



    def rectangle(
        self,
        rect,
        color
    ):

        pygame.draw.rect(
            self.surface,
            color,
            rect
        )
