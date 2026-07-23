"""
P.I.E. ADS7846 Touch Calibration

MPI3501 ILI9486
480x320 touchscreen
"""


class TouchCalibration:


    def __init__(self):

        # Measured raw calibration points
        self.raw_x_min = 0
        self.raw_x_max = 3892

        self.raw_y_min = 0
        self.raw_y_max = 3981

        self.width = 480
        self.height = 320



    def convert(self, x, y):


        #
        # Normalize raw values
        #

        screen_x = int(
            (x - self.raw_x_min) *
            479 /
            (self.raw_x_max - self.raw_x_min)
        )


        screen_y = int(
            (y - self.raw_y_min) *
            319 /
            (self.raw_y_max - self.raw_y_min)
        )



        #
        # Clamp
        #

        screen_x = max(
            0,
            min(
                479,
                screen_x
            )
        )


        screen_y = max(
            0,
            min(
                319,
                screen_y
            )
        )


        return screen_x, screen_y
