"""
P.I.E. Input Manager

Reads Linux evdev touchscreen events.
"""

import struct


class TouchInput:


    def __init__(self, device="/dev/input/event0"):

        self.device = device

        self.file = open(
            device,
            "rb"
        )

        self.x = 0
        self.y = 0



    def read(self):

        data = self.file.read(24)

        if len(data) != 24:
            return None


        (
            tv_sec,
            tv_usec,
            ev_type,
            ev_code,
            value
        ) = struct.unpack(
            "llHHI",
            data
        )


        # Absolute coordinates
        if ev_type == 3:

            if ev_code == 0:
                self.x = value

            elif ev_code == 1:
                self.y = value


        # Touch press/release
        if ev_type == 1:

            return {
                "x": self.x,
                "y": self.y,
                "pressed": value
            }


        return None
