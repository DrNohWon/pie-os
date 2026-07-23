"""
P.I.E. Home Screen
"""

import pygame

from pie_ui.widgets.label import Label
from pie_ui.widgets.button import Button



class HomeScreen:


    def __init__(self, renderer):

        self.renderer = renderer


        self.font_large = pygame.font.SysFont(
            "DejaVuSans",
            32
        )

        self.font = pygame.font.SysFont(
            "DejaVuSans",
            20
        )


        self.widgets = []


        self.widgets.append(
            Label(
                150,
                40,
                "P.I.E.",
                self.font_large
            )
        )


        self.widgets.append(
            Label(
                90,
                90,
                "Permanently",
                self.font
            )
        )


        self.widgets.append(
            Label(
                110,
                120,
                "Incomplete",
                self.font
            )
        )


        self.widgets.append(
            Label(
                120,
                150,
                "Environment",
                self.font
            )
        )


        self.launch = Button(
            150,
            220,
            180,
            50,
            "LAUNCH",
            self.font,
            self.launch_pressed
        )


        self.widgets.append(
            self.launch
        )



    def launch_pressed(self):

        print(
            "P.I.E. Launch pressed"
        )



    def draw(self):

        for widget in self.widgets:

            widget.draw(
                self.renderer
            )



    def touch(self,event):

        for widget in self.widgets:

            widget.touch(
                event
            )
