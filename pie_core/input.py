"""
P.I.E. Touch Input Handler

ADS7846 touchscreen input
non-blocking.
"""

import evdev
from evdev import ecodes

from pie_core.touch_calibration import TouchCalibration



class TouchInput:


    def __init__(self):

        self.device = evdev.InputDevice(
            "/dev/input/event0"
        )

        self.calibration = TouchCalibration()

        self.x = 0
        self.y = 0



    def read(self):

        try:

            events = self.device.read_one()


            if events is None:

                return None



            if events.type == ecodes.EV_ABS:


                if events.code == ecodes.ABS_X:

                    self.x = events.value


                elif events.code == ecodes.ABS_Y:

                    self.y = events.value



            elif events.type == ecodes.EV_KEY:


                if events.code == ecodes.BTN_TOUCH:


                    cx, cy = self.calibration.convert(
                        self.x,
                        self.y
                    )


                    return {

                        "x": cx,

                        "y": cy,

                        "pressed": events.value

                    }



        except Exception:

            return None



        return None
