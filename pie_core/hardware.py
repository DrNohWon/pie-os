"""
P.I.E. Hardware Abstraction Layer

Provides a unified interface
to Raspberry Pi hardware.
"""

import os
import platform


class Hardware:


    def __init__(self):

        self.system = platform.system()
        self.machine = platform.machine()


    def get_display(self):

        displays = []

        for fb in [
            "/dev/fb0",
            "/dev/fb1"
        ]:

            if os.path.exists(fb):
                displays.append(fb)

        return displays


    def get_cpu_temperature(self):

        try:

            with open(
                "/sys/class/thermal/thermal_zone0/temp",
                "r"
            ) as file:

                temp = int(file.read())

                return round(
                    temp / 1000,
                    1
                )

        except:

            return None


    def get_system_info(self):

        return {

            "system": self.system,

            "architecture": self.machine,

            "displays": self.get_display(),

            "cpu_temp": self.get_cpu_temperature()

        }
