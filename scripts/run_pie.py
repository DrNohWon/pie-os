#!/usr/bin/env python3

import sys
import os

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(
    0,
    PROJECT_ROOT
)


from pie_ui.display import Display
from pie_core.logger import Logger


log = Logger()

display = Display()

log.info(
    f"Display detected: {display.info()}"
)

print(
    display.info()
)
