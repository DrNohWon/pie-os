"""
P.I.E. Core Logger

Central logging system for:
Permanently Incomplete Environment
"""

import os
import datetime


LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "pie.log")


class Logger:

    def __init__(self):
        self.setup()


    def setup(self):
        os.makedirs(LOG_DIR, exist_ok=True)


    def write(self, level, message):

        timestamp = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        entry = (
            f"{timestamp} "
            f"[{level}] "
            f"{message}"
        )

        print(entry)

        with open(LOG_FILE, "a") as file:
            file.write(entry + "\n")


    def info(self, message):
        self.write(
            "INFO",
            message
        )


    def warning(self, message):
        self.write(
            "WARNING",
            message
        )


    def error(self, message):
        self.write(
            "ERROR",
            message
        )


    def boot(self, message):
        self.write(
            "BOOT",
            message
        )
