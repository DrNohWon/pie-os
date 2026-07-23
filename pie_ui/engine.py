"""
P.I.E. UI Engine

Software rendered UI engine.
"""

import pygame

from pie_ui.renderer import Renderer
from pie_ui.framebuffer import FrameBuffer

from pie_ui.screens.manager import ScreenManager
from pie_ui.screens.home import HomeScreen



class UIEngine:


    def __init__(self):

        pygame.init()


        # Initialize pygame event system
        pygame.display.set_mode(
            (
                1,
                1
            ),
            pygame.NOFRAME
        )


        self.surface = pygame.Surface(
            (
                480,
                320
            )
        )


        self.renderer = Renderer(
            self.surface
        )


        self.fb = FrameBuffer(
            "/dev/fb1"
        )


        self.screen_manager = ScreenManager()


        self.screen_manager.set_screen(
            HomeScreen(
                self.renderer
            )
        )



    def run(self):

        clock = pygame.time.Clock()


        running = True


        while running:


            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    running = False



            self.screen_manager.handle_events()


            self.renderer.clear(
                (
                    0,
                    0,
                    0
                )
            )


            self.screen_manager.draw()


            self.fb.write(
                self.surface
            )


            clock.tick(30)



        self.fb.close()

        pygame.quit()
