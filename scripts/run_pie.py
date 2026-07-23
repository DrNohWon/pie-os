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


from pie_core.boot import BootManager


boot = BootManager()

boot.start()
