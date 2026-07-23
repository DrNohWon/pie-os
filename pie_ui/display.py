"""
P.I.E. Display Manager

Handles framebuffer display output.
"""

import os


class Display:


    def __init__(self):

        self.device = "/dev/fb1"

        self.width = 480

        self.height = 320


    def exists(self):

        return os.path.exists(
            self.device
        )


    def info(self):

        return {

            "device": self.device,

            "width": self.width,

            "height": self.height,

            "available": self.exists()

        }
