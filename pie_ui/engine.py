"""
P.I.E. UI Engine

Main graphics loop.
Uses pygame as a drawing engine
and outputs directly to framebuffer.
"""

import pygame
import time

from pie_ui.renderer import Renderer
from pie_ui.framebuffer import FrameBuffer


class UIEngine:


    def __init__(self):

        pygame.init()


        # Off-screen drawing surface
        self.screen = pygame.Surface(
            (480, 320)
        )


        # Renderer layer
        self.renderer = Renderer(
            self.screen
        )


        # Direct framebuffer output
        self.fb = FrameBuffer(
            "/dev/fb1"
        )


        self.clock = pygame.time.Clock()


        self.running = True



    def run(self):

        font = pygame.font.SysFont(
            "DejaVuSans",
            28
        )


        while self.running:


            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    self.running = False



            # Background
            self.renderer.clear(
                (0,0,0)
            )


            # Boot title
            self.renderer.text(
                "P.I.E.",
                (165,80),
                font,
                (255,255,255)
            )


            # Status
            self.renderer.text(
                "Starting...",
                (130,140),
                font,
                (180,180,180)
            )


            # Push pixels to SPI screen
            self.fb.write(
                self.screen
            )


            self.clock.tick(30)


        self.fb.close()

        pygame.quit()
