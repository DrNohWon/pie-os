"""
P.I.E. ADS7846 Touch Calibration

MPI3501 ILI9486
480x320 rotated touchscreen
"""


class TouchCalibration:


    def __init__(self):

        self.raw_x_max = 3872
        self.raw_y_max = 3992

        self.width = 480
        self.height = 320



    def convert(self, x, y):


        raw_x = int(
            x * 480 /
            self.raw_x_max
        )

        raw_y = int(
            y * 320 /
            self.raw_y_max
        )


        #
        # 90 degree rotation
        #

        screen_x = (
            319 -
            raw_y
        )


        screen_y = int(
            raw_x *
            320 /
            480
        )


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
