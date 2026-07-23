"""
P.I.E. Framebuffer Output

RGB888 to RGB565 converter
for ILI9486 framebuffer.
"""

import pygame


class FrameBuffer:


    def __init__(self, device="/dev/fb1"):

        self.device = device

        self.file = open(
            device,
            "wb"
        )


    def rgb565(self, r, g, b):

        return (
            ((r & 0xF8) << 8) |
            ((g & 0xFC) << 3) |
            (b >> 3)
        )


    def write(self, surface):

        pixels = pygame.image.tostring(
            surface,
            "RGB"
        )


        output = bytearray()


        for i in range(
            0,
            len(pixels),
            3
        ):

            r = pixels[i]

            g = pixels[i+1]

            b = pixels[i+2]


            color = self.rgb565(
                r,
                g,
                b
            )


            # Linux framebuffer expects little endian
            output.append(
                color & 0xFF
            )

            output.append(
                color >> 8
            )


        self.file.seek(0)

        self.file.write(
            output
        )


    def close(self):

        self.file.close()
