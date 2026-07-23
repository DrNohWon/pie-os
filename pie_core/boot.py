"""
P.I.E. Boot Manager

Controls system startup sequence.
"""

from pie_core.logger import Logger
from pie_core.config import Config
from pie_core.hardware import Hardware
from pie_ui.display import Display
from pie_core.version import get_version


class BootManager:


    def __init__(self):

        self.logger = Logger()

        self.config = None

        self.hardware = None

        self.display = None


    def start(self):

        self.logger.boot(
            "Starting P.I.E. boot sequence"
        )


        self.load_version()

        self.load_config()

        self.detect_hardware()

        self.initialize_display()


        self.logger.boot(
            "P.I.E. system ready"
        )


    def load_version(self):

        self.logger.info(
            f"Version: {get_version()}"
        )


    def load_config(self):

        self.config = Config()

        self.logger.info(
            "Configuration loaded"
        )


    def detect_hardware(self):

        self.hardware = Hardware()

        info = self.hardware.get_system_info()

        self.logger.info(
            f"Hardware: {info}"
        )


    def initialize_display(self):

        self.display = Display()

        self.logger.info(
            f"Display: {self.display.info()}"
        )
